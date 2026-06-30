from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.company_financials import CompanyFinancials


class FinancialService:

    def __init__(self, db: Session):
        self.db = db

    def save_statement(
        self,
        ticker,
        statement_name,
        dataframe,
    ):

        inserted = 0

        for _, row in dataframe.iterrows():

            period = str(row["Period"].date())

            for column in dataframe.columns:

                if column == "Period":
                    continue

                value = row[column]

                if value is None:
                    continue

                try:

                    value = float(value)

                except Exception:
                    continue

                financial = CompanyFinancials(
                    ticker=ticker,
                    statement_type=statement_name,
                    metric=column,
                    period=period,
                    value=value,
                )

                self.db.add(financial)

                inserted += 1

        self.db.commit()

        logger.info(
            f"{statement_name}: {inserted} records inserted."
        )