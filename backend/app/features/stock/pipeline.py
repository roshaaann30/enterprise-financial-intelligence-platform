from app.features.stock.orchestrator import (
    StockFeatureOrchestrator,
)


class StockPipeline:

    @staticmethod
    def process(dataframe):

        return StockFeatureOrchestrator.process(
            dataframe
        )