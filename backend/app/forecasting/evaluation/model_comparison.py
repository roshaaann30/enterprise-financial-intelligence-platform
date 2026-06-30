class ModelComparison:

    @staticmethod
    def compare(results):

        print()

        print("=" * 70)

        print("MODEL COMPARISON")

        print("=" * 70)

        print(
            f"{'Model':20}"
            f"{'MAE':>12}"
            f"{'RMSE':>12}"
            f"{'R2':>12}"
            f"{'MAPE':>12}"
        )

        print("-" * 70)

        for model_name, metrics in results.items():

            print(

                f"{model_name:20}"

                f"{metrics['MAE']:12.3f}"

                f"{metrics['RMSE']:12.3f}"

                f"{metrics['R2']:12.3f}"

                f"{metrics['MAPE']:12.3f}"

            )