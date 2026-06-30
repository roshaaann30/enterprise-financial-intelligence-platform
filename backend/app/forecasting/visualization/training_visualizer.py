import matplotlib.pyplot as plt


class TrainingVisualizer:

    @staticmethod
    def plot_loss(history):

        plt.figure(figsize=(10, 5))

        plt.plot(

            history["train_loss"],

            label="Training Loss",

        )

        plt.plot(

            history["validation_loss"],

            label="Validation Loss",

        )

        plt.xlabel("Epoch")

        plt.ylabel("Loss")

        plt.title("Training History")

        plt.legend()

        plt.grid(True)

        plt.savefig(

            "app/forecasting/saved_models/training_loss.png"

        )

        plt.close()

    @staticmethod
    def plot_predictions(

        actual,

        predicted,

    ):

        plt.figure(figsize=(12, 6))

        plt.plot(

            actual,

            label="Actual",

        )

        plt.plot(

            predicted,

            label="Predicted",

        )

        plt.xlabel("Samples")

        plt.ylabel("Revenue")

        plt.title("Revenue Prediction")

        plt.legend()

        plt.grid(True)

        plt.savefig(

            "app/forecasting/saved_models/predictions.png"

        )

        plt.close()