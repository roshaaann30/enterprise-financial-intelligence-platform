import os
import optuna


class StudyManager:

    STORAGE_FOLDER = "app/forecasting/saved_studies"

    ##############################################################

    @staticmethod
    def create(

        study_name,

        direction="minimize",

    ):

        os.makedirs(

            StudyManager.STORAGE_FOLDER,

            exist_ok=True,

        )

        database = (

            f"sqlite:///"

            f"{StudyManager.STORAGE_FOLDER}/"

            f"{study_name}.db"

        )

        study = optuna.create_study(

            study_name=study_name,

            storage=database,

            direction=direction,

            load_if_exists=True,

        )

        return study

    ##############################################################

    @staticmethod
    def load(

        study_name,

    ):

        database = (

            f"sqlite:///"

            f"{StudyManager.STORAGE_FOLDER}/"

            f"{study_name}.db"

        )

        study = optuna.load_study(

            study_name=study_name,

            storage=database,

        )

        return study

    ##############################################################

    @staticmethod
    def resume(

        study_name,

        direction="minimize",

    ):

        return StudyManager.create(

            study_name,

            direction,

        )

    ##############################################################

    @staticmethod
    def delete(

        study_name,

    ):

        database = (

            f"{StudyManager.STORAGE_FOLDER}/"

            f"{study_name}.db"

        )

        if os.path.exists(

            database

        ):

            os.remove(

                database

            )

    ##############################################################

    @staticmethod
    def list_studies():

        os.makedirs(

            StudyManager.STORAGE_FOLDER,

            exist_ok=True,

        )

        studies = []

        for file in os.listdir(

            StudyManager.STORAGE_FOLDER

        ):

            if file.endswith(

                ".db"

            ):

                studies.append(

                    file.replace(

                        ".db",

                        "",

                    )

                )

        return studies

    ##############################################################

    @staticmethod
    def summary(

        study,

    ):

        print()

        print("=" * 70)

        print("STUDY SUMMARY")

        print("=" * 70)

        print()

        print(

            "Study Name:",

            study.study_name,

        )

        print()

        print(

            "Trials:",

            len(study.trials),

        )

        print()

        print(

            "Best Value:",

            study.best_value,

        )

        print()

        print("Best Parameters")

        print()

        for key, value in study.best_params.items():

            print(

                f"{key:<20}{value}"

            )

        print()

        print("=" * 70)