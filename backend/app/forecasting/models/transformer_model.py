import math

import torch
import torch.nn as nn


class PositionalEncoding(nn.Module):

    def __init__(
        self,
        d_model,
        max_length=5000,
    ):

        super().__init__()

        position = torch.arange(
            max_length,
            dtype=torch.float32,
        ).unsqueeze(1)

        div_term = torch.exp(

            torch.arange(
                0,
                d_model,
                2,
            ).float()

            * (-math.log(10000.0) / d_model)

        )

        pe = torch.zeros(

            max_length,

            d_model,

        )

        pe[:, 0::2] = torch.sin(

            position * div_term

        )

        pe[:, 1::2] = torch.cos(

            position * div_term

        )

        pe = pe.unsqueeze(0)

        self.register_buffer(

            "pe",

            pe,

        )

    def forward(
        self,
        x,
    ):

        return x + self.pe[
            :,
            : x.size(1),
        ]


##############################################################


class RevenueTransformer(nn.Module):

    def __init__(

        self,

        input_size,

        d_model=128,

        nhead=8,

        num_layers=4,

        dim_feedforward=256,

        dropout=0.2,

    ):

        super().__init__()

        #######################################################
        # Input Projection
        #######################################################

        self.embedding = nn.Linear(

            input_size,

            d_model,

        )

        #######################################################
        # Positional Encoding
        #######################################################

        self.position = PositionalEncoding(

            d_model

        )

        #######################################################
        # Transformer Encoder
        #######################################################

        encoder_layer = nn.TransformerEncoderLayer(

            d_model=d_model,

            nhead=nhead,

            dim_feedforward=dim_feedforward,

            dropout=dropout,

            batch_first=True,

        )

        self.encoder = nn.TransformerEncoder(

            encoder_layer,

            num_layers=num_layers,

        )

        #######################################################
        # Output Layers
        #######################################################

        self.dropout = nn.Dropout(

            dropout

        )

        self.fc1 = nn.Linear(

            d_model,

            64,

        )

        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(

            64,

            1,

        )

    ###########################################################

    def forward(

        self,

        x,

    ):

        #######################################################
        # Feature Embedding
        #######################################################

        x = self.embedding(

            x

        )

        #######################################################
        # Positional Encoding
        #######################################################

        x = self.position(

            x

        )

        #######################################################
        # Transformer Encoder
        #######################################################

        x = self.encoder(

            x

        )

        #######################################################
        # Last Time Step
        #######################################################

        x = x[:, -1, :]

        #######################################################
        # Dense Layers
        #######################################################

        x = self.dropout(

            x

        )

        x = self.fc1(

            x

        )

        x = self.relu(

            x

        )

        x = self.fc2(

            x

        )

        return x