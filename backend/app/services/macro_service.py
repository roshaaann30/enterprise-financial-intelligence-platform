from sqlalchemy.orm import Session

from app.models.macroeconomic_indicator import (
    MacroeconomicIndicator,
)


class MacroService:

    def __init__(self, db: Session):

        self.db = db

    def save_indicator(self, dataframe):

        for _, row in dataframe.iterrows():

            indicator = MacroeconomicIndicator(
                indicator=row["Indicator"],
                date=str(row["Date"].date()),
                value=float(row["Value"]),
                source=row["Source"],
            )

            self.db.add(indicator)

        self.db.commit()