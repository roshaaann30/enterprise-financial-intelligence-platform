from app.core.logger import logger
from app.services.dataset_version_service import DatasetVersionService
from app.services.feature_store_service import FeatureStoreService
from app.warehouse.warehouse import DataWarehouse


class FeaturePipelineOrchestrator:

    def __init__(self, db):

        self.db = db

        self.warehouse = DataWarehouse()

        self.feature_service = FeatureStoreService(db)

        self.dataset_service = DatasetVersionService(db)

    def run(
        self,
        ticker,
        dataframe,
    ):

        logger.info(
            f"Processing Feature Pipeline for {ticker}"
        )

        processed = self.warehouse.process_dataset(
            dataframe
        )

        self.feature_service.save_features(
            ticker,
            processed,
        )

        dataset = self.dataset_service.register_dataset(
            dataset_name=f"{ticker} Features",
            source="Yahoo Finance",
        )

        summary = self.warehouse.summarize_dataset(
            processed
        )

        logger.info(
            "Feature Pipeline Completed"
        )

        return {
            "dataset": dataset,
            "summary": summary,
        }