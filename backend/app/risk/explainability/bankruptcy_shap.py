import shap
import pandas as pd


class BankruptcySHAP:

    """
    Enterprise Bankruptcy SHAP Explainer
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

        model,

    ):

        self.model = model

        self.explainer = shap.TreeExplainer(

            model

        )

    ###########################################################
    # Explain Single Company
    ###########################################################

    def explain(

        self,

        features,

        top_n=10,

    ):

        shap_values = self.explainer.shap_values(

            features

        )

        values = shap_values[0]

        results = []

        for feature, value in zip(

            features.columns,

            values,

        ):

            results.append(

                {

                    "Feature": feature,

                    "Impact": float(value),

                    "AbsoluteImpact":

                        abs(float(value)),

                }

            )

        results = sorted(

            results,

            key=lambda x:

            x["AbsoluteImpact"],

            reverse=True,

        )

        return results[:top_n]

    ###########################################################
    # Global Importance
    ###########################################################

    def global_importance(

        self,

        features,

    ):

        shap_values = self.explainer.shap_values(

            features

        )

        importance = abs(

            shap_values

        ).mean(axis=0)

        results = []

        for feature, value in zip(

            features.columns,

            importance,

        ):

            results.append(

                {

                    "Feature": feature,

                    "Importance": float(value),

                }

            )

        results = sorted(

            results,

            key=lambda x:

            x["Importance"],

            reverse=True,

        )

        return pd.DataFrame(

            results

        )