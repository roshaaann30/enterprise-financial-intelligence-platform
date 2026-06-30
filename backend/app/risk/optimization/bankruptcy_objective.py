from sklearn.metrics import (
    roc_auc_score,
)

from app.risk.models.bankruptcy_model import (
    BankruptcyModel,
)

from app.risk.trainers.bankruptcy_trainer import (
    BankruptcyTrainer,
)


class BankruptcyObjective:

    ###########################################################
    # Objective Function
    ###########################################################

    @staticmethod
    def objective(

        trial,

        X_train,

        y_train,

        X_test,

        y_test,

    ):

        #######################################################
        # Hyperparameters
        #######################################################

        params = {

            "learning_rate":

                trial.suggest_float(

                    "learning_rate",

                    0.001,

                    0.2,

                    log=True,

                ),

            "max_depth":

                trial.suggest_int(

                    "max_depth",

                    3,

                    10,

                ),

            "n_estimators":

                trial.suggest_int(

                    "n_estimators",

                    100,

                    1000,

                ),

            "subsample":

                trial.suggest_float(

                    "subsample",

                    0.5,

                    1.0,

                ),

            "colsample_bytree":

                trial.suggest_float(

                    "colsample_bytree",

                    0.5,

                    1.0,

                ),

        }

        #######################################################
        # Model
        #######################################################

        model = BankruptcyModel(

            learning_rate=params[
                "learning_rate"
            ],

            max_depth=params[
                "max_depth"
            ],

            n_estimators=params[
                "n_estimators"
            ],

            subsample=params[
                "subsample"
            ],

            colsample_bytree=params[
                "colsample_bytree"
            ],

        )

        #######################################################
        # Train
        #######################################################

        trainer = BankruptcyTrainer(

            model

        )

        trainer.train(

            X_train,

            y_train,

        )

        #######################################################
        # Evaluate
        #######################################################

        probabilities = model.predict_proba(

            X_test

        )

        score = roc_auc_score(

            y_test,

            probabilities,

        )

        #######################################################
        # Save Metrics
        #######################################################

        trial.set_user_attr(

            "ROC_AUC",

            float(score),

        )

        return float(score)