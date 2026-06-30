class FinancialExplainer:

    """
    Explain Financial Changes
    """

    @staticmethod
    def explain(

        metric,

        current,

        previous,

    ):

        change = (

            current

            - previous

        )

        percent = (

            change

            /

            previous

            * 100

        )

        return {

            "metric":

                metric,

            "change":

                round(

                    change,

                    2,

                ),

            "percent_change":

                round(

                    percent,

                    2,

                ),

        }