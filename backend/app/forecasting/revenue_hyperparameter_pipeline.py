from app.forecasting.optimization.optuna_optimizer import (
    OptunaOptimizer,
)

from app.forecasting.optimization.study_manager import (
    StudyManager,
)

from app.forecasting.optimization.objective_functions import (
    ForecastObjectiveFunctions,
)


class RevenueHyperparameterPipeline:

    @staticmethod
    def optimize(

        model_name,

        pipeline,

        train_df,

        validation_df,

        objective_function,

        n_trials=30,

    ):

        ##########################################################
        # Create / Resume Study
        ##########################################################

        StudyManager.create(

            study_name=model_name,

        )

        ##########################################################
        # Optimizer
        ##########################################################

        optimizer = OptunaOptimizer(

            study_name=model_name,

            storage=f"sqlite:///app/forecasting/saved_studies/{model_name}.db",

        )

        ##########################################################
        # Objective Wrapper
        ##########################################################

        def objective(trial):

            return objective_function(

                trial,

                pipeline,

                train_df,

                validation_df,

            )

        ##########################################################
        # Optimize
        ##########################################################

        study = optimizer.optimize(

            objective,

            n_trials=n_trials,

        )

        ##########################################################
        # Save Study
        ##########################################################

        optimizer.save()

        ##########################################################
        # Summary
        ##########################################################

        optimizer.print_summary()

        ##########################################################
        # Return Results
        ##########################################################

        return {

            "study": study,

            "best_params": optimizer.best_parameters(),

            "best_score": optimizer.best_score(),

            "best_trial": optimizer.best_trial(),

        }

    ##############################################################

    @staticmethod

    def optimize_lstm(

        train_df,

        validation_df,

        pipeline,

        n_trials=30,

    ):

        return RevenueHyperparameterPipeline.optimize(

            model_name="lstm",

            pipeline=pipeline,

            train_df=train_df,

            validation_df=validation_df,

            objective_function=ForecastObjectiveFunctions.optimize_lstm,

            n_trials=n_trials,

        )

    ##############################################################

    @staticmethod

    def optimize_gru(

        train_df,

        validation_df,

        pipeline,

        n_trials=30,

    ):

        return RevenueHyperparameterPipeline.optimize(

            model_name="gru",

            pipeline=pipeline,

            train_df=train_df,

            validation_df=validation_df,

            objective_function=ForecastObjectiveFunctions.optimize_gru,

            n_trials=n_trials,

        )

    ##############################################################

    @staticmethod

    def optimize_transformer(

        train_df,

        validation_df,

        pipeline,

        n_trials=30,

    ):

        return RevenueHyperparameterPipeline.optimize(

            model_name="transformer",

            pipeline=pipeline,

            train_df=train_df,

            validation_df=validation_df,

            objective_function=ForecastObjectiveFunctions.optimize_transformer,

            n_trials=n_trials,

        )

    ##############################################################

    @staticmethod

    def optimize_xgboost(

        train_df,

        validation_df,

        pipeline,

        n_trials=30,

    ):

        return RevenueHyperparameterPipeline.optimize(

            model_name="xgboost",

            pipeline=pipeline,

            train_df=train_df,

            validation_df=validation_df,

            objective_function=ForecastObjectiveFunctions.optimize_xgboost,

            n_trials=n_trials,

        )

    ##############################################################

    @staticmethod

    def optimize_lightgbm(

        train_df,

        validation_df,

        pipeline,

        n_trials=30,

    ):

        return RevenueHyperparameterPipeline.optimize(

            model_name="lightgbm",

            pipeline=pipeline,

            train_df=train_df,

            validation_df=validation_df,

            objective_function=ForecastObjectiveFunctions.optimize_lightgbm,

            n_trials=n_trials,

        )

    ##############################################################

    @staticmethod

    def optimize_catboost(

        train_df,

        validation_df,

        pipeline,

        n_trials=30,

    ):

        return RevenueHyperparameterPipeline.optimize(

            model_name="catboost",

            pipeline=pipeline,

            train_df=train_df,

            validation_df=validation_df,

            objective_function=ForecastObjectiveFunctions.optimize_catboost,

            n_trials=n_trials,

        )