import torch
import torch.nn as nn


class RevenueGRU(nn.Module):

    def __init__(
        self,
        input_size,
        hidden_size=128,
        num_layers=2,
        dropout=0.2,
    ):

        super().__init__()

        self.hidden_size = hidden_size

        self.num_layers = num_layers

        ##########################################################
        # GRU Layer
        ##########################################################

        self.gru = nn.GRU(

            input_size=input_size,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            dropout=dropout,

        )

        ##########################################################
        # Regularization
        ##########################################################

        self.dropout = nn.Dropout(
            dropout
        )

        ##########################################################
        # Fully Connected Layers
        ##########################################################

        self.fc1 = nn.Linear(

            hidden_size,

            64,

        )

        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(

            64,

            1,

        )

    ##############################################################

    def forward(
        self,
        x,
    ):

        ##########################################################
        # GRU Forward Pass
        ##########################################################

        output, hidden = self.gru(
            x
        )

        ##########################################################
        # Last Hidden State
        ##########################################################

        x = hidden[-1]

        ##########################################################
        # Dropout
        ##########################################################

        x = self.dropout(
            x
        )

        ##########################################################
        # Dense Layer
        ##########################################################

        x = self.fc1(
            x
        )

        x = self.relu(
            x
        )

        ##########################################################
        # Revenue Prediction
        ##########################################################

        x = self.fc2(
            x
        )

        return x