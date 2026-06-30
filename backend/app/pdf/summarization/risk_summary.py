class RiskSummary:

    """
    Generate Risk Summary
    """

    @staticmethod
    def generate(

        risks,

    ):

        if not risks:

            return (

                "No significant risks identified."

            )

        summary = (

            f"{len(risks)} risks detected.\n\n"

        )

        for risk in risks:

            summary += (

                f"- "

                f"{risk['risk_type']} "

                f"({risk['severity']})\n"

            )

        return summary