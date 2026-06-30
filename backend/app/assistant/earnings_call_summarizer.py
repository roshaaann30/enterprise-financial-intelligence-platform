class EarningsCallSummarizer:

    """
    Earnings Call Summary
    """

    @staticmethod
    def summarize(

        transcript,

    ):

        return {

            "summary":

                transcript[:2000],

            "length":

                len(

                    transcript

                ),

        }