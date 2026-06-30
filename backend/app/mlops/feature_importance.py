class FeatureImportanceEngine:

    @staticmethod
    def extract(

        model,

        feature_names,

    ):

        if hasattr(

            model,

            "feature_importances_",

        ):

            return dict(

                zip(

                    feature_names,

                    model.feature_importances_,

                )

            )

        return {}