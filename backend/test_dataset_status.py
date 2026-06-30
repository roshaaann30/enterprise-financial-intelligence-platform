from app.database.session import SessionLocal
from app.services.dataset_version_service import DatasetVersionService

db = SessionLocal()

service = DatasetVersionService(db)

dataset = service.update_status(
    dataset_id=1,
    status="ARCHIVED",
)

print(dataset.status)

db.close()