class BullAnalyst:

    """
    Bull Investment Analyst
    """

    @staticmethod
    def analyze(

        context,

    ):

        research = context.get(

            "research_findings",

            {}

        )

        opportunities = research.get(

            "opportunities",

            []

        )

        outlook = research.get(

            "outlook",

            {}

        )

        arguments = []

        #######################################################
        # Opportunities
        #######################################################

        for item in opportunities:

            arguments.append(

                f"Growth opportunity: "

                f"{item.get('opportunity_type')}"

            )

        #######################################################
        # Outlook
        #######################################################

        if outlook:

            arguments.append(

                f"Positive outlook: "

                f"{outlook}"

            )

        #######################################################
        # Recommendation
        #######################################################

        return {

            "stance":

                "Bullish",

            "arguments":

                arguments,

        }