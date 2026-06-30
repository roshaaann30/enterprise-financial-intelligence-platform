import pandas as pd
from fredapi import Fred

from app.core.settings import settings
from app.core.logger import logger


class MacroFeatureGenerator:

    def __init__(self):

        self.fred = Fred(
            api_key=settings.FRED_API_KEY
        )

    def generate(self):

        logger.info("Downloading Macroeconomic Data...")

        data = pd.DataFrame()

        try:

            data["FedFundsRate"] = self.fred.get_series(
                "FEDFUNDS"
            )

            logger.info("Fed Funds Rate Loaded")

            data["CPI"] = self.fred.get_series(
                "CPIAUCSL"
            )

            logger.info("CPI Loaded")

            data["UnemploymentRate"] = self.fred.get_series(
                "UNRATE"
            )

            logger.info("Unemployment Rate Loaded")

            data["GDP"] = self.fred.get_series(
                "GDP"
            )

            logger.info("GDP Loaded")

            data["Treasury10Y"] = self.fred.get_series(
                "DGS10"
            )

            logger.info("10-Year Treasury Loaded")

            data["Treasury2Y"] = self.fred.get_series(
                "DGS2"
            )

            logger.info("2-Year Treasury Loaded")

            data["VIX"] = self.fred.get_series(
                "VIXCLS"
            )

            logger.info("VIX Loaded")

            data["OilPrice"] = self.fred.get_series(
                "DCOILWTICO"
            )

            logger.info("Oil Price Loaded")

            

            data["DollarIndex"] = self.fred.get_series(
                "DTWEXBGS"
            )

            logger.info("Dollar Index Loaded")

        except Exception as e:

            logger.exception(
                f"Macroeconomic Data Download Failed: {str(e)}"
            )

            raise

        data.index.name = "Date"

        data.reset_index(inplace=True)

        data["Date"] = pd.to_datetime(
            data["Date"]
        )

        data = data.sort_values(
            by="Date"
        )

        data = data.ffill()

        data = data.bfill()

        logger.info(
            f"Downloaded {len(data)} macroeconomic records."
        )

        return data