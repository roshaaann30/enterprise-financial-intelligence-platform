from sqlalchemy.orm import Session

from app.models.data_quality_report import DataQualityReport


class DataQualityService:

    def __init__(self, db: Session):
        self.db = db

    def save_report(
        self,
        dataset,
        check_type,
        status,
        message,
    ):

        report = DataQualityReport(
            dataset=dataset,
            check_type=check_type,
            status=status,
            message=message,
        )

        self.db.add(report)

        self.db.commit()