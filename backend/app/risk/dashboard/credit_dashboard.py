class CreditDashboard:

    """
    Enterprise Credit Dashboard Formatter
    """

    ###########################################################
    # Single Borrower Report
    ###########################################################

    @staticmethod
    def borrower_report(

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

                    "direction":

                        "Increases Risk"

                        if item["Impact"] > 0

                        else "Reduces Risk",

                }

            )

        return {

            "credit_score":

                prediction[
                    "credit_score"
                ],

            "risk_category":

                prediction[
                    "risk_category"
                ],

            "default_probability":

                round(

                    prediction[
                        "default_probability"
                    ],

                    4,

                ),

            "default_percentage":

                prediction[
                    "default_percentage"
                ],

            "confidence":

                prediction[
                    "confidence"
                ],

            "top_risk_factors":

                top_factors,

        }

    ###########################################################
    # Portfolio Report
    ###########################################################

    @staticmethod
    def portfolio_report(

        predictions,

    ):

        excellent = 0
        very_good = 0
        good = 0
        fair = 0
        poor = 0

        for item in predictions:

            category = item["RiskCategory"]

            if category == "Excellent":
                excellent += 1

            elif category == "Very Good":
                very_good += 1

            elif category == "Good":
                good += 1

            elif category == "Fair":
                fair += 1

            else:
                poor += 1

        return {

            "summary": {

                "borrowers":

                    len(predictions),

                "excellent":

                    excellent,

                "very_good":

                    very_good,

                "good":

                    good,

                "fair":

                    fair,

                "poor":

                    poor,

            },

            "predictions":

                predictions,

        }