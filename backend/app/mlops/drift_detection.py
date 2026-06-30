import numpy as np

from scipy.stats import ks_2samp


class DriftDetectionEngine:

    @staticmethod
    def detect(

        reference_data,

        current_data,

    ):

        statistic,

        p_value = (

            ks_2samp(

                reference_data,

                current_data,

            )

        )

        return {

            "drift_detected":

                p_value < 0.05,

            "p_value":

                float(

                    p_value

                ),

            "statistic":

                float(

                    statistic

                ),

        }