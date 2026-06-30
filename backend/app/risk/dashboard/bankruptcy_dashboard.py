class BankruptcyDashboard:

    """
    Enterprise Bankruptcy Dashboard Formatter
    """

    ###########################################################
    # Single Company Report
    ###########################################################

    @staticmethod
    def company_report(

        prediction,

        shap_results,

    ):

        top_factors = []

        for item in shap_results:

            top_factors.append(

                {

                    "feature":

                        item["Feature"],

                    "impact":

                        round(

                            item["Impact"],

                            4,

                        ),

                }

            )

        return {

            "bankruptcy_probability":

                round(

                    prediction[
                        "bankruptcy_probability"
                    ],

                    4,

                ),

            "bankruptcy_percentage":

                prediction[
                    "bankruptcy_percentage"
                ],

            "risk_level":

                prediction[
                    "risk_level"
                ],

            "confidence":

                prediction[
                    "confidence"
                ],

            "top_risk_factors":

                top_factors,

        }

    ###########################################################
    # Batch Report
    ###########################################################

    @staticmethod
    def batch_report(

        predictions,

    ):

        total = len(

            predictions

        )

        low = 0
        moderate = 0
        high = 0
        critical = 0

        for item in predictions:

            risk = item["Risk"]

            if risk == "Low":
                low += 1

            elif risk == "Moderate":
                moderate += 1

            elif risk == "High":
                high += 1

            else:
                critical += 1

        return {

            "summary": {

                "companies":

                    total,

                "low_risk":

                    low,

                "moderate_risk":

                    moderate,

                "high_risk":

                    high,

                "critical_risk":

                    critical,

            },

            "predictions":

                predictions,

        }