import numpy as np
import torch

from app.forecasting.models.transformer_model import (
    RevenueTransformer,
)

from app.forecasting.preprocessing.scaler import (
    ForecastScaler,
)

from app.forecasting.preprocessing.sequence_builder import (
    SequenceBuilder,
)


class RevenueTransformerPredictor:

    def __init__(self):

        ###########################################################
        # Device
        ###########################################################

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

        model_path="app/forecasting/saved_models/revenue_transformer.pt",

    ):

        ###########################################################
        # Create Transformer
        ###########################################################

        self.model = RevenueTransformer(

            input_size=input_size,

            d_model=128,

            nhead=8,

            num_layers=4,

            dim_feedforward=256,

            dropout=0.2,

        )

        ###########################################################
        # Load Weights
        ###########################################################

        self.model.load_state_dict(

            torch.load(

                model_path,

                map_location=self.device,

            )

        )

        ###########################################################
        # Evaluation Mode
        ###########################################################

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
        # Scale Features
        ###########################################################

        X = self.scaler.transform_features(

            dataframe

        )

        ###########################################################
        # Build Sequences
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
        # Convert Prediction Back
        ###########################################################

        prediction = prediction.cpu().numpy()

        prediction = self.scaler.inverse_target(

            prediction

        )

        return prediction.flatten()