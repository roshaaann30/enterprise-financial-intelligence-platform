import pandas as pd
import yfinance as yf

from app.core.logger import logger


class FinancialsIngestion:

    def fetch_income_statement(self, ticker: str) -> pd.DataFrame:

        logger.info(f"Downloading Income Statement for {ticker}")

        company = yf.Ticker(ticker)

        dataframe = company.financials.T

        if dataframe.empty:
            raise Exception(f"Income Statement not found for {ticker}")

        dataframe.reset_index(inplace=True)

        dataframe.rename(columns={"index": "Period"}, inplace=True)

        return dataframe

    def fetch_balance_sheet(self, ticker: str) -> pd.DataFrame:

        logger.info(f"Downloading Balance Sheet for {ticker}")

        company = yf.Ticker(ticker)

        dataframe = company.balance_sheet.T

        if dataframe.empty:
            raise Exception(f"Balance Sheet not found for {ticker}")

        dataframe.reset_index(inplace=True)

        dataframe.rename(columns={"index": "Period"}, inplace=True)

        return dataframe

    def fetch_cash_flow(self, ticker: str) -> pd.DataFrame:

        logger.info(f"Downloading Cash Flow for {ticker}")

        company = yf.Ticker(ticker)

        dataframe = company.cashflow.T

        if dataframe.empty:
            raise Exception(f"Cash Flow not found for {ticker}")

        dataframe.reset_index(inplace=True)

        dataframe.rename(columns={"index": "Period"}, inplace=True)

        return dataframe

    def fetch_company_info(self, ticker: str) -> dict:

        logger.info(f"Downloading Company Information for {ticker}")

        company = yf.Ticker(ticker)

        return company.info