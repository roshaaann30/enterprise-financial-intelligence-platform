from sqlalchemy.orm import Session

from app.models.processed_dataset import ProcessedDataset
from app.warehouse.version_manager import VersionManager


class DatasetVersionService:

    def __init__(self, db: Session):

        self.db = db

    def register_dataset(
        self,
        dataset_name,
        source,
    ):

        dataset = ProcessedDataset(
            dataset_name=dataset_name,
            dataset_version=VersionManager.generate_version(),
            source=source,
            status="SUCCESS",
        )

        self.db.add(dataset)
        self.db.commit()
        self.db.refresh(dataset)

        return dataset

    def get_dataset(
        self,
        dataset_id,
    ):

        return (
            self.db.query(ProcessedDataset)
            .filter(
                ProcessedDataset.id == dataset_id
            )
            .first()
        )

    def get_all_datasets(self):

        return self.db.query(
            ProcessedDataset
        ).all()

    def update_status(
        self,
        dataset_id,
        status,
    ):

        dataset = self.get_dataset(
            dataset_id
        )

        if dataset:

            dataset.status = status

            self.db.commit()

        return dataset