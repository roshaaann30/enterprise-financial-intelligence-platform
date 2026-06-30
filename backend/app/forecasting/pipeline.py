from app.forecasting.dataset_builder import (
    ForecastDatasetBuilder,
)


class ForecastPipeline:

    @staticmethod
    def build(
        stock_df,
        financial_df,
        macro_df,
        news_df,
    ):

        return ForecastDatasetBuilder.build(
            stock_df,
            financial_df,
            macro_df,
            news_df,
        )