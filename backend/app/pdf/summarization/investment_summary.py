class InvestmentSummary:

    """
    Investment Opportunity Summary
    """

    @staticmethod
    def generate(

        opportunities,

        outlook,

    ):

        summary = ""

        summary += (

            f"Business Outlook: "

            f"{outlook['outlook']}\n\n"

        )

        summary += (

            f"Detected "

            f"{len(opportunities)} "

            f"growth opportunities.\n"

        )

        for item in opportunities:

            summary += (

                f"- "

                f"{item['opportunity_type']} "

                f"({item['strength']})\n"

            )

        return summary