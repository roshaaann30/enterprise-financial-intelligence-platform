from app.forecasting.merger import (
    DatasetMerger,
)

from app.forecasting.targets import (
    ForecastTargetGenerator,
)

from app.forecasting.splitter import (
    TimeSeriesSplitter,
)


class ForecastDatasetBuilder:

    @staticmethod
    def build(
        stock_df,
        financial_df,
        macro_df,
        news_df,
    ):

        dataset = DatasetMerger.merge(
            stock_df,
            financial_df,
            macro_df,
            news_df,
        )

        dataset = (
            ForecastTargetGenerator
            .create_targets(dataset)
        )

        dataset = dataset.dropna()

        train, validation, test = (
            TimeSeriesSplitter.split(
                dataset
            )
        )

        return {
            "dataset": dataset,
            "train": train,
            "validation": validation,
            "test": test,
        }