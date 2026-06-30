from datetime import datetime

from app.mlops.confidence_engine import (
    ConfidenceEngine,
)

from app.mlops.feature_importance import (
    FeatureImportanceEngine,
)

from app.mlops.prediction_monitor import (
    PredictionMonitor,
)

from app.mlops.drift_detection import (
    DriftDetectionEngine,
)

from app.mlops.model_registry import (
    ModelRegistry,
)


class EnterpriseMonitoringManager:

    """
    Enterprise Explainable AI
    and Model Monitoring Platform
    """

    ###########################################################
    # Monitor Prediction
    ###########################################################

    @staticmethod
    def monitor_prediction(

        model_name,

        prediction,

        probabilities,

        features=None,

    ):

        confidence = (

            ConfidenceEngine.calculate(

                probabilities

            )

        )

        PredictionMonitor.log(

            model_name,

            prediction,

            confidence,

        )

        return {

            "timestamp":

                datetime.now()

                .isoformat(),

            "model":

                model_name,

            "prediction":

                prediction,

            "confidence":

                confidence,

            "features":

                features or {},

        }

    ###########################################################
    # Feature Importance
    ###########################################################

    @staticmethod
    def explain_model(

        model_name,

        feature_names,

    ):

        model = (

            ModelRegistry.get(

                model_name

            )

        )

        if model is None:

            return {

                "error":

                    "Model not found"

            }

        importance = (

            FeatureImportanceEngine

            .extract(

                model,

                feature_names,

            )

        )

        return {

            "model":

                model_name,

            "feature_importance":

                importance,

        }

    ###########################################################
    # Drift Detection
    ###########################################################

    @staticmethod
    def detect_drift(

        reference_data,

        current_data,

    ):

        result = (

            DriftDetectionEngine

            .detect(

                reference_data,

                current_data,

            )

        )

        alert = None

        if result[

            "drift_detected"

        ]:

            alert = (

                "Model retraining recommended"

            )

        return {

            **result,

            "alert":

                alert,

        }

    ###########################################################
    # Model Health
    ###########################################################

    @staticmethod
    def model_health(

        model_name,

        accuracy,

        drift_detected,

    ):

        score = 100

        score -= (

            (1 - accuracy)

            * 100

        )

        if drift_detected:

            score -= 20

        score = max(

            0,

            round(

                score,

                2,

            ),

        )

        if score >= 90:

            status = "Healthy"

        elif score >= 70:

            status = "Monitor"

        else:

            status = "Retrain"

        return {

            "model":

                model_name,

            "health_score":

                score,

            "status":

                status,

        }

    ###########################################################
    # Monitoring Dashboard
    ###########################################################

    @staticmethod
    def dashboard():

        logs = (

            PredictionMonitor

            .get_logs()

        )

        total_predictions = (

            len(logs)

        )

        if total_predictions == 0:

            avg_confidence = 0

        else:

            avg_confidence = round(

                sum(

                    item["confidence"]

                    for item in logs

                )

                /

                total_predictions,

                2,

            )

        return {

            "registered_models":

                ModelRegistry

                .list_models(),

            "prediction_volume":

                total_predictions,

            "average_confidence":

                avg_confidence,

            "recent_predictions":

                logs[-10:],

        }