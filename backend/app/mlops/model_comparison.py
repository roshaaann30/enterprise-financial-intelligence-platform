class ModelComparisonEngine:

    @staticmethod
    def compare(

        results,

    ):

        best_model = max(

            results,

            key=lambda x:

            x["accuracy"]

        )

        return {

            "best_model":

                best_model,

            "all_models":

                results,

        }