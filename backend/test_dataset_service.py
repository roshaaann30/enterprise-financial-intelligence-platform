from app.database.session import SessionLocal
from app.services.dataset_version_service import DatasetVersionService

db = SessionLocal()

service = DatasetVersionService(db)

datasets = service.get_all_datasets()

for dataset in datasets:

    print(
        dataset.id,
        dataset.dataset_name,
        dataset.dataset_version,
        dataset.status,
    )

db.close()