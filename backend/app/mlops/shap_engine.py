import shap


class SHAPEngine:

    @staticmethod
    def explain(

        model,

        data,

    ):

        explainer = (

            shap.Explainer(

                model,

                data,

            )

        )

        shap_values = (

            explainer(

                data

            )

        )

        return shap_values