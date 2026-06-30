from app.core.logger import logger

from app.features.stock.technical_indicators import (
    TechnicalIndicatorGenerator,
)
from app.features.stock.momentum_indicators import (
    MomentumIndicatorGenerator,
)
from app.features.stock.trend_indicators import (
    TrendIndicatorGenerator,
)
from app.features.stock.volatility_indicators import (
    VolatilityIndicatorGenerator,
)
from app.features.stock.volume_indicators import (
    VolumeIndicatorGenerator,
)
from app.features.stock.time_series_features import (
    TimeSeriesFeatureGenerator,
)

from app.features.stock.rolling_features import (
    RollingFeatureGenerator,
)

from app.features.stock.lag_features import (
    LagFeatureGenerator,
)

class StockFeatureOrchestrator:

    @staticmethod
    def process(dataframe):

        logger.info("=" * 70)
        logger.info("STOCK FEATURE ENGINEERING STARTED")
        logger.info("=" * 70)

        try:

            logger.info("Generating Technical Indicators...")
            dataframe = TechnicalIndicatorGenerator.generate(
                dataframe
            )

            logger.info("Generating Momentum Indicators...")
            dataframe = MomentumIndicatorGenerator.generate(
                dataframe
            )

            logger.info("Generating Trend Indicators...")
            dataframe = TrendIndicatorGenerator.generate(
                dataframe
            )

            logger.info("Generating Volatility Indicators...")
            dataframe = VolatilityIndicatorGenerator.generate(
                dataframe
            )

            logger.info("Generating Volume Indicators...")
            dataframe = VolumeIndicatorGenerator.generate(
                dataframe
            )

            logger.info("Generating Time-Series Features...")

            dataframe = TimeSeriesFeatureGenerator.generate(
                dataframe
            )

            logger.info("Generating Rolling Statistics...")

            dataframe = RollingFeatureGenerator.generate(
                dataframe
            )

            logger.info("Generating Lag Features...")

            dataframe = LagFeatureGenerator.generate(
                dataframe
            )

            logger.info("Cleaning Feature Dataset...")

            dataframe = dataframe.loc[
                :,
                ~dataframe.columns.duplicated()
            ]

            dataframe = dataframe.bfill()

            dataframe = dataframe.ffill()

            if dataframe.isnull().sum().sum() > 0:
                raise ValueError(
                    "Null values still exist after feature engineering."
                )

            if len(dataframe.columns) != len(set(dataframe.columns)):
                raise ValueError(
                    "Duplicate feature columns detected."
                )

            logger.info(
                f"Feature Engineering Completed Successfully"
            )

            logger.info(
                f"Total Features : {len(dataframe.columns)}"
            )

            logger.info(
                f"Total Rows : {len(dataframe)}"
            )

            logger.info("=" * 70)

            return dataframe

        except Exception as e:

            logger.exception(
                f"Feature Engineering Failed : {str(e)}"
            )

            raise