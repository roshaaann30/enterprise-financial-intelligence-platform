class CompanyComparison:

    """
    Compare Two Companies
    """

    @staticmethod
    def compare(

        company_a,

        company_b,

    ):

        metrics_a = company_a.get(

            "metrics",

            {},

        )

        metrics_b = company_b.get(

            "metrics",

            {},

        )

        return {

            "company_a":

                company_a.get(

                    "company"

                ),

            "company_b":

                company_b.get(

                    "company"

                ),

            "metrics_a":

                metrics_a,

            "metrics_b":

                metrics_b,

        }