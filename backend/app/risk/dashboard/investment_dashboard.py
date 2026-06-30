class InvestmentDashboard:

    """
    Enterprise Investment Dashboard
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

                    "direction":

                        "Positive"

                        if item["Impact"] > 0

                        else "Negative",

                }

            )

        return {

            "investment_score":

                prediction[
                    "investment_score"
                ],

            "recommendation":

                prediction[
                    "recommendation"
                ],

            "risk_probability":

                prediction[
                    "risk_probability"
                ],

            "risk_percentage":

                prediction[
                    "risk_percentage"
                ],

            "risk_category":

                prediction[
                    "risk_category"
                ],

            "expected_return":

                prediction[
                    "expected_return"
                ],

            "confidence":

                prediction[
                    "confidence"
                ],

            "top_factors":

                top_factors,

        }

    ###########################################################
    # Portfolio Report
    ###########################################################

    @staticmethod
    def portfolio_report(

        predictions,

    ):

        buy = 0
        hold = 0
        sell = 0

        for item in predictions:

            recommendation = item[

                "recommendation"

            ]

            if recommendation == "BUY":

                buy += 1

            elif recommendation == "HOLD":

                hold += 1

            else:

                sell += 1

        return {

            "summary": {

                "companies":

                    len(predictions),

                "buy":

                    buy,

                "hold":

                    hold,

                "sell":

                    sell,

            },

            "predictions":

                predictions,

        }