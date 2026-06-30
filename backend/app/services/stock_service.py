from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.stock_price import StockPrice


class StockService:

    def __init__(self, db: Session):
        self.db = db

    def save_stock_prices(self, dataframe):

        inserted = 0
        skipped = 0

        for _, row in dataframe.iterrows():

            stock = StockPrice(
                ticker=row["Ticker"],
                date=row["Date"].date(),
                open_price=float(row["Open"]),
                high_price=float(row["High"]),
                low_price=float(row["Low"]),
                close_price=float(row["Close"]),
                volume=int(row["Volume"]),
            )

            try:
                self.db.add(stock)
                self.db.commit()
                inserted += 1

            except IntegrityError:
                self.db.rollback()
                skipped += 1

        logger.info(
            f"Inserted: {inserted} | Skipped: {skipped}"
        )