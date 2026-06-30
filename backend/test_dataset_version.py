from app.database.session import SessionLocal
from app.services.dataset_version_service import (
    DatasetVersionService,
)

db = SessionLocal()

service = DatasetVersionService(db)

dataset = service.register_dataset(
    dataset_name="AAPL Features",
    source="Yahoo Finance",
)

print(dataset.dataset_version)

db.close()