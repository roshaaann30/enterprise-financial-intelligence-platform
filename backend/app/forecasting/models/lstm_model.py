import torch
import torch.nn as nn


class RevenueLSTM(nn.Module):

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

        self.lstm = nn.LSTM(

            input_size=input_size,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            dropout=dropout,

        )

        self.dropout = nn.Dropout(
            dropout
        )

        self.fc1 = nn.Linear(
            hidden_size,
            64,
        )

        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(
            64,
            1,
        )

    def forward(
        self,
        x,
    ):

        output, (hidden, cell) = self.lstm(
            x
        )

        x = hidden[-1]

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