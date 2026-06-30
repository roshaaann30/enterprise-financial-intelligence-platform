import os
import joblib
import optuna


class OptunaOptimizer:

    def __init__(

        self,

        study_name,

        direction="minimize",

        storage=None,

    ):

        self.study_name = study_name

        self.direction = direction

        self.storage = storage

        ##########################################################

        # Create Study

        ##########################################################

        self.study = optuna.create_study(

            study_name=study_name,

            direction=direction,

            storage=storage,

            load_if_exists=True,

        )

    ##############################################################

    def optimize(

        self,

        objective,

        n_trials=30,

        timeout=None,

    ):

        self.study.optimize(

            objective,

            n_trials=n_trials,

            timeout=timeout,

        )

        return self.study

    ##############################################################

    def best_parameters(

        self,

    ):

        return self.study.best_params

    ##############################################################

    def best_score(

        self,

    ):

        return self.study.best_value

    ##############################################################

    def best_trial(

        self,

    ):

        return self.study.best_trial

    ##############################################################

    def save(

        self,

        folder="app/forecasting/saved_models",

    ):

        os.makedirs(

            folder,

            exist_ok=True,

        )

        joblib.dump(

            self.study,

            os.path.join(

                folder,

                f"{self.study_name}.pkl",

            ),

        )

    ##############################################################

    @staticmethod

    def load(

        study_path,

    ):

        return joblib.load(

            study_path

        )

    ##############################################################

    def print_summary(

        self,

    ):

        print()

        print("=" * 70)

        print("OPTUNA OPTIMIZATION SUMMARY")

        print("=" * 70)

        print()

        print(

            "Study :",

            self.study.study_name,

        )

        print()

        print(

            "Trials:",

            len(

                self.study.trials

            ),

        )

        print()

        print(

            "Best Score:",

            self.study.best_value,

        )

        print()

        print("Best Parameters")

        print()

        for key, value in self.study.best_params.items():

            print(

                f"{key:<20}{value}"

            )

        print()

        print("=" * 70)