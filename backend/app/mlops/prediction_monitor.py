from datetime import datetime


class PredictionMonitor:

    LOGS = []

    @classmethod
    def log(

        cls,

        model_name,

        prediction,

        confidence,

    ):

        cls.LOGS.append(

            {

                "timestamp":

                    datetime.now()

                    .isoformat(),

                "model":

                    model_name,

                "prediction":

                    prediction,

                "confidence":

                    confidence,

            }

        )

    @classmethod
    def get_logs(

        cls,

    ):

        return cls.LOGS