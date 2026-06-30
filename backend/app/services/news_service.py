from sqlalchemy.orm import Session

from app.models.financial_news import FinancialNews


class NewsService:

    def __init__(self, db: Session):
        self.db = db

    def save_news(self, articles):

        for article in articles:

            news = FinancialNews(
                ticker=article["ticker"],
                title=article["title"],
                publisher=article["publisher"],
                published_at=article["published_at"],
                article_url=article["article_url"],
                summary=article["summary"],
            )

            self.db.add(news)

        self.db.commit()