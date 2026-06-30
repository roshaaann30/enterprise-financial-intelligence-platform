from app.features.financial.ratios import (
    FinancialFeatureGenerator,
)

from app.features.financial.growth import (
    GrowthFeatureGenerator,
)


class FinancialPipeline:

    @staticmethod
    def process(dataframe):

        dataframe = FinancialFeatureGenerator.generate(
            dataframe
        )

        dataframe = GrowthFeatureGenerator.generate(
            dataframe
        )

        return dataframe