class RiskDashboard:

    """
    Risk Dashboard Generator
    """

    @staticmethod
    def generate(

        analysis,

    ):

        return {

            "overall_risk_score":

                analysis[

                    "risk_score"

                ],

            "risk_count":

                len(

                    analysis["risks"]

                ),

            "high_risks":

                [

                    r

                    for r in analysis["risks"]

                    if r["severity"]

                    == "High"

                ],

            "all_risks":

                analysis["risks"],

        }