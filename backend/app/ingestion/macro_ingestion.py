import pandas as pd
from fredapi import Fred

from app.core.logger import logger
from app.core.settings import settings


class MacroIngestion:

    def __init__(self):

        self.fred = Fred(api_key=settings.FRED_API_KEY)

    def fetch_indicator(
        self,
        fred_code,
        indicator_name,
    ):

        logger.info(f"Downloading {indicator_name}")

        data = self.fred.get_series(fred_code)

        dataframe = pd.DataFrame(data)

        dataframe.reset_index(inplace=True)

        dataframe.columns = [
            "Date",
            "Value",
        ]

        dataframe["Indicator"] = indicator_name

        dataframe["Source"] = "FRED"

        return dataframe