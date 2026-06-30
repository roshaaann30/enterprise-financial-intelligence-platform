class BearAnalyst:

    """
    Bear Investment Analyst
    """

    @staticmethod
    def analyze(

        context,

    ):

        research = context.get(

            "research_findings",

            {}

        )

        risks = research.get(

            "risks",

            []

        )

        arguments = []

        #######################################################
        # Risks
        #######################################################

        for risk in risks:

            arguments.append(

                f"Risk identified: "

                f"{risk.get('risk_type')}"

            )

        #######################################################
        # Recommendation
        #######################################################

        return {

            "stance":

                "Bearish",

            "arguments":

                arguments,

        }