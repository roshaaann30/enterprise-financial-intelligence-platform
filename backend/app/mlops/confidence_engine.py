import numpy as np


class ConfidenceEngine:

    @staticmethod
    def calculate(

        probabilities,

    ):

        confidence = (

            np.max(

                probabilities

            )

            * 100

        )

        return round(

            float(

                confidence

            ),

            2,

        )