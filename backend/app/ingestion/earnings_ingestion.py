from app.core.logger import logger


class EarningsIngestion:

    def fetch_transcript(
        self,
        ticker: str,
    ):

        logger.info(f"Fetching transcript for {ticker}")

        return {
            "ticker": ticker,
            "fiscal_year": 2025,
            "quarter": "Q4",
            "transcript": (
                f"Placeholder earnings transcript for {ticker}. "
                "Replace with a real transcript provider later."
            ),
        }