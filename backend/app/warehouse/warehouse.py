from app.core.logger import logger
from app.warehouse.dataset_manager import DatasetManager
from app.warehouse.feature_pipeline import FeaturePipeline


class DataWarehouse:

    def __init__(self):

        self.dataset_manager = DatasetManager()

        logger.info(
            "Enterprise Data Warehouse Initialized"
        )

    def process_dataset(
        self,
        dataframe,
    ):

        return FeaturePipeline.generate_features(
            dataframe
        )

    def summarize_dataset(
        self,
        dataframe,
    ):

        return self.dataset_manager.summarize_dataset(
            dataframe
        )