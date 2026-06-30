from app.core.logger import logger


class DatasetManager:

    def __init__(self):

        logger.info("Dataset Manager Initialized")

    def summarize_dataset(
        self,
        dataframe,
    ):

        return {
            "rows": len(dataframe),
            "columns": len(dataframe.columns),
            "column_names": list(dataframe.columns),
        }