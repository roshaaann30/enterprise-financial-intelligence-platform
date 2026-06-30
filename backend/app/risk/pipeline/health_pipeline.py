import pandas as pd

from app.risk.feature_pipeline import (
    RiskFeaturePipeline,
)

from app.risk.scoring.category_scores import (
    CategoryScores,
)

from app.risk.scoring.health_score import (
    FinancialHealthScore,
)

from app.risk.scoring.health_classifier import (
    HealthClassifier,
)


class HealthPipeline:

    """
    Enterprise Financial Health Pipeline

    Pipeline Flow

    Raw Financial Statements
            │
            ▼
    Financial Ratio Engine
            │
            ▼
    Category Scores
            │
            ▼
    Financial Health Score
            │
            ▼
    Health Classification
    """

    @staticmethod
    def process(df):

        ##########################################################
        # Generate Financial Features
        ##########################################################

        feature_result = RiskFeaturePipeline.process(df)

        features = feature_result["features"]

        ##########################################################
        # Calculate Category Scores
        ##########################################################

        category_scores = []

        for _, row in features.iterrows():

            scores = CategoryScores.calculate(row)

            category_scores.append(scores)

        category_scores = pd.DataFrame(category_scores)

        ##########################################################
        # Calculate Overall Health Score
        ##########################################################

        health_engine = FinancialHealthScore()

        health_dataframe = health_engine.calculate_dataframe(

            category_scores

        )

        ##########################################################
        # Health Classification
        ##########################################################

        classified = HealthClassifier.classify_dataframe(

            health_dataframe

        )

        ##########################################################
        # Merge Results
        ##########################################################

        result = pd.concat(

            [

                df.reset_index(drop=True),

                features.reset_index(drop=True),

                classified.reset_index(drop=True),

            ],

            axis=1,

        )

        ##########################################################
        # Summary
        ##########################################################

        summary = {

            "Companies": len(result),

            "AverageHealthScore": float(

                result["FinancialHealthScore"].mean()

            ),

            "MaximumHealthScore": float(

                result["FinancialHealthScore"].max()

            ),

            "MinimumHealthScore": float(

                result["FinancialHealthScore"].min()

            ),

            "HealthDistribution":

                HealthClassifier.summary(

                    classified

                )

        }

        ##########################################################
        # Return
        ##########################################################

        return {

            "data": result,

            "summary": summary,

        }