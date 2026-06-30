class CompanyQualityDashboard:

    """
    Enterprise Company Quality Dashboard
    """

    ###########################################################
    # Company Report
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

            "quality_score":

                prediction[
                    "quality_score"
                ],

            "rating":

                prediction[
                    "rating"
                ],

            "recommendation":

                prediction[
                    "recommendation"
                ],

            "confidence":

                prediction[
                    "confidence"
                ],

            "inputs":

                prediction[
                    "inputs"
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

        elite = 0
        excellent = 0
        good = 0
        average = 0
        weak = 0
        poor = 0

        for item in predictions:

            rating = item["rating"]

            if rating == "Elite":

                elite += 1

            elif rating == "Excellent":

                excellent += 1

            elif rating == "Good":

                good += 1

            elif rating == "Average":

                average += 1

            elif rating == "Weak":

                weak += 1

            else:

                poor += 1

        return {

            "summary": {

                "companies":

                    len(predictions),

                "elite":

                    elite,

                "excellent":

                    excellent,

                "good":

                    good,

                "average":

                    average,

                "weak":

                    weak,

                "poor":

                    poor,

            },

            "predictions":

                predictions,

        }