from app.core.logger import logger
from app.database.session import SessionLocal

from app.ingestion.stock_ingestion import StockIngestion
from app.ingestion.financials_ingestion import FinancialsIngestion
from app.ingestion.earnings_ingestion import EarningsIngestion
from app.ingestion.news_ingestion import NewsIngestion

from app.services.stock_service import StockService
from app.services.financial_service import FinancialService
from app.services.earnings_service import EarningsService
from app.services.news_service import NewsService


TICKERS = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "META",
    "NVDA",
    "TSLA",
]


def run_pipeline():

    logger.info("=" * 80)
    logger.info("ENTERPRISE FINANCIAL DATA INGESTION PIPELINE STARTED")
    logger.info("=" * 80)

    db = SessionLocal()

    stock_ingestion = StockIngestion()
    financial_ingestion = FinancialsIngestion()
    earnings_ingestion = EarningsIngestion()
    news_ingestion = NewsIngestion()

    stock_service = StockService(db)
    financial_service = FinancialService(db)
    earnings_service = EarningsService(db)
    news_service = NewsService(db)

    successful = 0
    failed = 0

    try:

        for ticker in TICKERS:

            logger.info("")
            logger.info("=" * 60)
            logger.info(f"Processing {ticker}")
            logger.info("=" * 60)

            try:

                # =====================================================
                # Historical Stock Prices
                # =====================================================

                stock_df = stock_ingestion.fetch_stock_prices(
                    ticker=ticker,
                    period="5y",
                )

                stock_service.save_stock_prices(stock_df)

                logger.info("Stock Prices Completed")

                # =====================================================
                # Income Statement
                # =====================================================

                income_df = financial_ingestion.fetch_income_statement(
                    ticker
                )

                financial_service.save_statement(
                    ticker=ticker,
                    statement_name="Income Statement",
                    dataframe=income_df,
                )

                logger.info("Income Statement Completed")

                # =====================================================
                # Balance Sheet
                # =====================================================

                balance_df = financial_ingestion.fetch_balance_sheet(
                    ticker
                )

                financial_service.save_statement(
                    ticker=ticker,
                    statement_name="Balance Sheet",
                    dataframe=balance_df,
                )

                logger.info("Balance Sheet Completed")

                # =====================================================
                # Cash Flow Statement
                # =====================================================

                cashflow_df = financial_ingestion.fetch_cash_flow(
                    ticker
                )

                financial_service.save_statement(
                    ticker=ticker,
                    statement_name="Cash Flow",
                    dataframe=cashflow_df,
                )

                logger.info("Cash Flow Statement Completed")

                # =====================================================
                # Company Information
                # =====================================================

                company_info = financial_ingestion.fetch_company_info(
                    ticker
                )

                logger.info(
                    f"Company : {company_info.get('longName', ticker)}"
                )

                logger.info(
                    f"Sector : {company_info.get('sector', 'Unknown')}"
                )

                logger.info(
                    f"Industry : {company_info.get('industry', 'Unknown')}"
                )

                logger.info("Company Information Completed")

                # =====================================================
                # Earnings Transcript
                # =====================================================

                transcript = earnings_ingestion.fetch_transcript(
                    ticker
                )

                earnings_service.save_transcript(
                    transcript
                )

                logger.info("Earnings Transcript Completed")

                # =====================================================
                # Financial News
                # =====================================================

                articles = news_ingestion.fetch_news(
                    ticker
                )

                news_service.save_news(
                    articles
                )

                logger.info("Financial News Completed")

                # =====================================================
                # Macroeconomic Indicators
                # =====================================================

                macro_indicators = {
                    "GDP": "GDP",
                    "Inflation": "CPIAUCSL",
                    "Interest Rate": "FEDFUNDS",
                    "Unemployment": "UNRATE",
                }

                for indicator_name, fred_code in macro_indicators.items():
                    dataframe = macro_ingestion.fetch_indicator(
                    fred_code=fred_code,
                    indicator_name=indicator_name,
                    )

                macro_service.save_indicator(
                    dataframe
                    )

                logger.info("Macroeconomic Indicators Completed")

                successful += 1

                logger.info(f"{ticker} Completed Successfully")

                orchestrator.run (
                    ticker,
                    stock_df,
                )
            except Exception as e:

                failed += 1

                logger.exception(
                    f"{ticker} Failed: {str(e)}"
                )

        logger.info("")
        logger.info("=" * 80)
        logger.info("PIPELINE SUMMARY")
        logger.info("=" * 80)

        logger.info(f"Successful Companies : {successful}")
        logger.info(f"Failed Companies     : {failed}")
        logger.info(f"Total Companies      : {len(TICKERS)}")

    finally:

        db.close()

        logger.info("")
        logger.info("=" * 80)
        logger.info("PIPELINE FINISHED")
        logger.info("=" * 80)


if __name__ == "__main__":
    run_pipeline()