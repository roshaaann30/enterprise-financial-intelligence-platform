from datetime import datetime

import yfinance as yf

from app.core.logger import logger


class NewsIngestion:

    def fetch_news(self, ticker: str):

        logger.info(f"Downloading News : {ticker}")

        company = yf.Ticker(ticker)

        news = company.news

        articles = []

        for article in news:

            articles.append(
                {
                    "ticker": ticker,
                    "title": article.get("title", ""),
                    "publisher": article.get("publisher", ""),
                    "published_at": datetime.fromtimestamp(
                        article.get("providerPublishTime", 0)
                    ),
                    "article_url": article.get("link", ""),
                    "summary": article.get("summary", ""),
                }
            )

        return articles