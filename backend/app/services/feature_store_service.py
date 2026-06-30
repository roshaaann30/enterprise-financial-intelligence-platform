from sqlalchemy.orm import Session

from app.models.feature_store import FeatureStore


class FeatureStoreService:

    def __init__(self, db: Session):

        self.db = db

    def save_features(
        self,
        ticker,
        dataframe,
    ):

        for _, row in dataframe.iterrows():

            features = {
                "Daily_Return": row["Daily_Return"],
                "MA_5": row["MA_5"],
                "MA_20": row["MA_20"],
                "Volatility": row["Volatility"],
            }

            for feature_name, value in features.items():

                feature = FeatureStore(
                    ticker=ticker,
                    feature_name=feature_name,
                    feature_value=float(value),
                    feature_version="v1",
                )

                self.db.add(feature)

        self.db.commit()