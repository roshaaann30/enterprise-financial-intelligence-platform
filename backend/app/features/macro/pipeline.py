from app.features.macro.macro_features import (
    MacroFeatureGenerator,
)


class MacroPipeline:

    @staticmethod
    def process():

        generator = MacroFeatureGenerator()

        return generator.generate()