class SearchSpaces:

    ############################################################
    # XGBoost
    ############################################################

    @staticmethod
    def xgboost(trial):

        return {

            "learning_rate": trial.suggest_float(
                "learning_rate",
                0.001,
                0.3,
                log=True,
            ),

            "max_depth": trial.suggest_int(
                "max_depth",
                3,
                12,
            ),

            "n_estimators": trial.suggest_int(
                "n_estimators",
                100,
                1000,
                step=100,
            ),

            "subsample": trial.suggest_float(
                "subsample",
                0.5,
                1.0,
            ),

            "colsample_bytree": trial.suggest_float(
                "colsample_bytree",
                0.5,
                1.0,
            ),

            "gamma": trial.suggest_float(
                "gamma",
                0.0,
                5.0,
            ),

        }

    ############################################################
    # LightGBM
    ############################################################

    @staticmethod
    def lightgbm(trial):

        return {

            "learning_rate": trial.suggest_float(
                "learning_rate",
                0.001,
                0.3,
                log=True,
            ),

            "num_leaves": trial.suggest_int(
                "num_leaves",
                15,
                255,
            ),

            "max_depth": trial.suggest_int(
                "max_depth",
                3,
                15,
            ),

            "n_estimators": trial.suggest_int(
                "n_estimators",
                100,
                1000,
                step=100,
            ),

            "feature_fraction": trial.suggest_float(
                "feature_fraction",
                0.5,
                1.0,
            ),

            "bagging_fraction": trial.suggest_float(
                "bagging_fraction",
                0.5,
                1.0,
            ),

        }

    ############################################################
    # CatBoost
    ############################################################

    @staticmethod
    def catboost(trial):

        return {

            "learning_rate": trial.suggest_float(
                "learning_rate",
                0.001,
                0.3,
                log=True,
            ),

            "depth": trial.suggest_int(
                "depth",
                4,
                10,
            ),

            "iterations": trial.suggest_int(
                "iterations",
                200,
                1200,
                step=100,
            ),

            "l2_leaf_reg": trial.suggest_float(
                "l2_leaf_reg",
                1,
                10,
            ),

        }

    ############################################################
    # LSTM
    ############################################################

    @staticmethod
    def lstm(trial):

        return {

            "learning_rate": trial.suggest_float(
                "learning_rate",
                1e-5,
                1e-2,
                log=True,
            ),

            "hidden_size": trial.suggest_categorical(
                "hidden_size",
                [64, 128, 256, 512],
            ),

            "dropout": trial.suggest_float(
                "dropout",
                0.1,
                0.5,
            ),

            "num_layers": trial.suggest_int(
                "num_layers",
                1,
                4,
            ),

            "batch_size": trial.suggest_categorical(
                "batch_size",
                [16, 32, 64],
            ),

            "epochs": trial.suggest_int(
                "epochs",
                20,
                100,
            ),

        }

    ############################################################
    # GRU
    ############################################################

    @staticmethod
    def gru(trial):

        return {

            "learning_rate": trial.suggest_float(
                "learning_rate",
                1e-5,
                1e-2,
                log=True,
            ),

            "hidden_size": trial.suggest_categorical(
                "hidden_size",
                [64, 128, 256, 512],
            ),

            "dropout": trial.suggest_float(
                "dropout",
                0.1,
                0.5,
            ),

            "num_layers": trial.suggest_int(
                "num_layers",
                1,
                4,
            ),

            "batch_size": trial.suggest_categorical(
                "batch_size",
                [16, 32, 64],
            ),

            "epochs": trial.suggest_int(
                "epochs",
                20,
                100,
            ),

        }

    ############################################################
    # Transformer
    ############################################################

    @staticmethod
    def transformer(trial):

        return {

            "learning_rate": trial.suggest_float(
                "learning_rate",
                1e-5,
                1e-3,
                log=True,
            ),

            "d_model": trial.suggest_categorical(
                "d_model",
                [64, 128, 256],
            ),

            "nhead": trial.suggest_categorical(
                "nhead",
                [2, 4, 8],
            ),

            "num_layers": trial.suggest_int(
                "num_layers",
                2,
                6,
            ),

            "dropout": trial.suggest_float(
                "dropout",
                0.1,
                0.5,
            ),

            "batch_size": trial.suggest_categorical(
                "batch_size",
                [16, 32, 64],
            ),

            "epochs": trial.suggest_int(
                "epochs",
                20,
                100,
            ),

        }

    ############################################################
    # Ensemble
    ############################################################

    @staticmethod
    def ensemble(trial):

        weights = {

            "linear": trial.suggest_float("linear", 0, 1),

            "xgboost": trial.suggest_float("xgboost", 0, 1),

            "lightgbm": trial.suggest_float("lightgbm", 0, 1),

            "catboost": trial.suggest_float("catboost", 0, 1),

            "lstm": trial.suggest_float("lstm", 0, 1),

            "gru": trial.suggest_float("gru", 0, 1),

            "transformer": trial.suggest_float("transformer", 0, 1),

        }

        total = sum(weights.values())

        return {

            key: value / total

            for key, value in weights.items()

        }