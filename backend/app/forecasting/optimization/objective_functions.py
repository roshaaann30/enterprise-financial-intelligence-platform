import optuna

from app.forecasting.evaluation.regression_metrics import (
    RegressionMetrics,
)


class ForecastObjectiveFunctions:

    ##############################################################
    # Generic Regression Objective
    ##############################################################

    @staticmethod
    def regression_objective(

        trial,

        pipeline,

        train_df,

        validation_df,

    ):

        ##########################################################
        # Hyperparameters
        ##########################################################

        params = {

            "learning_rate": trial.suggest_float(

                "learning_rate",

                0.0001,

                0.1,

                log=True,

            ),

            "hidden_size": trial.suggest_categorical(

                "hidden_size",

                [

                    64,

                    128,

                    256,

                ],

            ),

            "dropout": trial.suggest_float(

                "dropout",

                0.1,

                0.5,

            ),

            "num_layers": trial.suggest_int(

                "num_layers",

                2,

                4,

            ),

            "batch_size": trial.suggest_categorical(

                "batch_size",

                [

                    16,

                    32,

                    64,

                ],

            ),

            "epochs": trial.suggest_int(

                "epochs",

                20,

                80,

            ),

        }

        ##########################################################
        # Train Pipeline
        ##########################################################

        result = pipeline.train(

            train_df,

            validation_df,

            params=params,

        )

        ##########################################################
        # Evaluate
        ##########################################################

        metrics = RegressionMetrics.evaluate(

            result["actuals"],

            result["predictions"],

        )

        ##########################################################
        # Convert NumPy values to Python floats
        ##########################################################

        mae = float(metrics["MAE"])

        rmse = float(metrics["RMSE"])

        mape = float(metrics["MAPE"])

        r2 = float(metrics["R2"])

        ##########################################################
        # Store Metrics
        ##########################################################

        trial.set_user_attr(

            "MAE",

            mae,

        )

        trial.set_user_attr(

            "RMSE",

            rmse,

        )

        trial.set_user_attr(

            "MAPE",

            mape,

        )

        trial.set_user_attr(

            "R2",

            r2,

        )

        ##########################################################
        # Objective
        ##########################################################

        return rmse

    ##############################################################
    # LSTM
    ##############################################################

    @staticmethod
    def optimize_lstm(

        trial,

        pipeline,

        train_df,

        validation_df,

    ):

        return ForecastObjectiveFunctions.regression_objective(

            trial,

            pipeline,

            train_df,

            validation_df,

        )

    ##############################################################
    # GRU
    ##############################################################

    @staticmethod
    def optimize_gru(

        trial,

        pipeline,

        train_df,

        validation_df,

    ):

        return ForecastObjectiveFunctions.regression_objective(

            trial,

            pipeline,

            train_df,

            validation_df,

        )

    ##############################################################
    # Transformer
    ##############################################################

    @staticmethod
    def optimize_transformer(

        trial,

        pipeline,

        train_df,

        validation_df,

    ):

        return ForecastObjectiveFunctions.regression_objective(

            trial,

            pipeline,

            train_df,

            validation_df,

        )

    ##############################################################
    # XGBoost
    ##############################################################

    @staticmethod
    def optimize_xgboost(

        trial,

        pipeline,

        train_df,

        validation_df,

    ):

        return ForecastObjectiveFunctions.regression_objective(

            trial,

            pipeline,

            train_df,

            validation_df,

        )

    ##############################################################
    # LightGBM
    ##############################################################

    @staticmethod
    def optimize_lightgbm(

        trial,

        pipeline,

        train_df,

        validation_df,

    ):

        return ForecastObjectiveFunctions.regression_objective(

            trial,

            pipeline,

            train_df,

            validation_df,

        )

    ##############################################################
    # CatBoost
    ##############################################################

    @staticmethod
    def optimize_catboost(

        trial,

        pipeline,

        train_df,

        validation_df,

    ):

        return ForecastObjectiveFunctions.regression_objective(

            trial,

            pipeline,

            train_df,

            validation_df,

        )