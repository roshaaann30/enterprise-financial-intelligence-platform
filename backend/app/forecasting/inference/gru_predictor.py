import numpy as np
import torch

from app.forecasting.models.gru_model import (
    RevenueGRU,
)

from app.forecasting.preprocessing.scaler import (
    ForecastScaler,
)

from app.forecasting.preprocessing.sequence_builder import (
    SequenceBuilder,
)


class RevenueGRUPredictor:

    def __init__(self):

        self.device = torch.device(

            "cuda"

            if torch.cuda.is_available()

            else "cpu"

        )

        ###########################################################
        # Load Scalers
        ###########################################################

        self.scaler = ForecastScaler()

        self.scaler.load()

        ###########################################################
        # Model Placeholder
        ###########################################################

        self.model = None

    ###############################################################

    def load_model(

        self,

        input_size,

        model_path="app/forecasting/saved_models/revenue_gru.pt",

    ):

        self.model = RevenueGRU(

            input_size=input_size,

        )

        self.model.load_state_dict(

            torch.load(

                model_path,

                map_location=self.device,

            )

        )

        self.model.to(

            self.device

        )

        self.model.eval()

    ###############################################################

    def predict(

        self,

        dataframe,

    ):

        ###########################################################
        # Feature Scaling
        ###########################################################

        X = self.scaler.transform_features(

            dataframe

        )

        ###########################################################
        # Sequence Generation
        ###########################################################

        dummy_target = np.zeros(

            len(X)

        )

        X_sequence, _ = SequenceBuilder.build(

            X,

            dummy_target,

        )

        ###########################################################
        # Tensor Conversion
        ###########################################################

        X_tensor = torch.tensor(

            X_sequence,

            dtype=torch.float32,

        ).to(

            self.device

        )

        ###########################################################
        # Prediction
        ###########################################################

        with torch.no_grad():

            prediction = self.model(

                X_tensor

            )

        ###########################################################
        # Convert Back To Revenue
        ###########################################################

        prediction = prediction.cpu().numpy()

        prediction = self.scaler.inverse_target(

            prediction

        )

        return prediction.flatten()