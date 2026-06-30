import time

import pandas as pd
import yfinance as yf

from app.core.logger import logger


class StockIngestion:

    def fetch_stock_prices(
        self,
        ticker: str,
        period: str = "5y",
    ) -> pd.DataFrame:

        start_time = time.time()

        try:
            logger.info(f"Downloading {ticker}...")

            stock = yf.Ticker(ticker)

            dataframe = stock.history(period=period)

            if dataframe.empty:
                raise Exception(f"No data found for {ticker}")

            dataframe.reset_index(inplace=True)

            dataframe["Ticker"] = ticker

            dataframe = dataframe[
                [
                    "Ticker",
                    "Date",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Volume",
                ]
            ]

            dataframe.dropna(inplace=True)

            dataframe.drop_duplicates(inplace=True)

            elapsed = round(time.time() - start_time, 2)

            logger.info(
                f"{ticker} downloaded successfully | "
                f"Rows: {len(dataframe)} | "
                f"Time: {elapsed}s"
            )

            return dataframe

        except Exception as e:
            logger.exception(f"{ticker} download failed")
            raise e