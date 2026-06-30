class DecisionAgent:

    """
    Investment Committee Agent
    """

    @staticmethod
    def decide(

        debate,

    ):

        bull_count = len(

            debate["bull_case"]

            ["arguments"]

        )

        bear_count = len(

            debate["bear_case"]

            ["arguments"]

        )

        #######################################################
        # Recommendation
        #######################################################

        if bull_count > bear_count:

            recommendation = (

                "Buy"

            )

        elif bear_count > bull_count:

            recommendation = (

                "Sell"

            )

        else:

            recommendation = (

                "Hold"

            )

        #######################################################
        # Confidence
        #######################################################

        total = (

            bull_count

            +

            bear_count

        )

        confidence = (

            50

            if total == 0

            else round(

                max(

                    bull_count,

                    bear_count,

                )

                /

                total

                * 100,

                2,

            )

        )

        return {

            "recommendation":

                recommendation,

            "confidence":

                confidence,

            "supporting_evidence":

                debate,

        }