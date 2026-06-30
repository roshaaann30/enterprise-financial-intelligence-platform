class ModelRegistry:

    MODELS = {}

    @classmethod
    def register(

        cls,

        model_name,

        model,

    ):

        cls.MODELS[

            model_name

        ] = model

    @classmethod
    def get(

        cls,

        model_name,

    ):

        return cls.MODELS.get(

            model_name

        )

    @classmethod
    def list_models(

        cls,

    ):

        return list(

            cls.MODELS.keys()

        )