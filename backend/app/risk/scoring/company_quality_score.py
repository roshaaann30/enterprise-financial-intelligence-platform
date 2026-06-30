class CompanyQualityScore:

    """
    Enterprise Company Quality Score Engine
    """

    ###########################################################
    # Rating
    ###########################################################

    @staticmethod
    def rating(

        score,

    ):

        if score >= 90:

            return "Elite"

        elif score >= 80:

            return "Excellent"

        elif score >= 70:

            return "Good"

        elif score >= 60:

            return "Average"

        elif score >= 40:

            return "Weak"

        else:

            return "Poor"

    ###########################################################
    # Recommendation
    ###########################################################

    @staticmethod
    def recommendation(

        score,

    ):

        if score >= 90:

            return "World Class Company"

        elif score >= 80:

            return "Strong Company"

        elif score >= 70:

            return "Stable Company"

        elif score >= 60:

            return "Monitor Closely"

        elif score >= 40:

            return "High Risk"

        else:

            return "Avoid"

    ###########################################################
    # Confidence
    ###########################################################

    @staticmethod
    def confidence(

        quality_score,

    ):

        confidence = (

            50

            +

            (quality_score / 2)

        )

        return min(

            100,

            round(

                confidence,

                2,

            ),

        )

    ###########################################################
    # Calculate
    ###########################################################

    @staticmethod
    def calculate(

        financial_health_score,

        bankruptcy_risk,

        credit_risk,

        investment_score,

    ):

        #######################################################
        # Weighted Quality Score
        #######################################################

        quality_score = (

            financial_health_score * 0.35

            +

            investment_score * 0.30

            +

            (100 - credit_risk) * 0.20

            +

            (100 - bankruptcy_risk) * 0.15

        )

        quality_score = round(

            quality_score,

            2,

        )

        #######################################################
        # Rating
        #######################################################

        rating = (

            CompanyQualityScore.rating(

                quality_score

            )

        )

        #######################################################
        # Recommendation
        #######################################################

        recommendation = (

            CompanyQualityScore.recommendation(

                quality_score

            )

        )

        #######################################################
        # Confidence
        #######################################################

        confidence = (

            CompanyQualityScore.confidence(

                quality_score

            )

        )

        #######################################################
        # Output
        #######################################################

        return {

            "quality_score":

                quality_score,

            "rating":

                rating,

            "recommendation":

                recommendation,

            "confidence":

                confidence,

            "components": {

                "financial_health":

                    financial_health_score,

                "investment_score":

                    investment_score,

                "credit_risk":

                    credit_risk,

                "bankruptcy_risk":

                    bankruptcy_risk,

            },

        }