from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)


class BankruptcyTrainer:

    """
    Enterprise Bankruptcy Trainer
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

        model,

    ):

        self.model = model

    ###########################################################
    # Train
    ###########################################################

    def train(

        self,

        X_train,

        y_train,

    ):

        self.model.fit(

            X_train,

            y_train,

        )

        return self.model

    ###########################################################
    # Evaluate
    ###########################################################

    def evaluate(

        self,

        X_test,

        y_test,

    ):

        #######################################################
        # Predictions
        #######################################################

        predictions = self.model.predict(

            X_test

        )

        probabilities = self.model.predict_proba(

            X_test

        )

        #######################################################
        # Metrics
        #######################################################

        metrics = {

            "Accuracy": float(

                accuracy_score(

                    y_test,

                    predictions,

                )

            ),

            "Precision": float(

                precision_score(

                    y_test,

                    predictions,

                    zero_division=0,

                )

            ),

            "Recall": float(

                recall_score(

                    y_test,

                    predictions,

                    zero_division=0,

                )

            ),

            "F1": float(

                f1_score(

                    y_test,

                    predictions,

                    zero_division=0,

                )

            ),

            "ROC_AUC": float(

                roc_auc_score(

                    y_test,

                    probabilities,

                )

            ),

        }

        #######################################################
        # Confusion Matrix
        #######################################################

        cm = confusion_matrix(

            y_test,

            predictions,

        )

        #######################################################
        # Classification Report
        #######################################################

        report = classification_report(

            y_test,

            predictions,

            output_dict=True,

            zero_division=0,

        )

        #######################################################
        # Return
        #######################################################

        return {

            "metrics": metrics,

            "confusion_matrix": cm.tolist(),

            "classification_report": report,

            "predictions": predictions,

            "probabilities": probabilities,

        }