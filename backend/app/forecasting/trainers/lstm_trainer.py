import os

import torch
import torch.nn as nn


class LSTMTrainer:

    def __init__(
        self,
        model,
        learning_rate=0.001,
        patience=5,
    ):

        self.device = torch.device(

            "cuda"

            if torch.cuda.is_available()

            else "cpu"

        )

        self.model = model.to(
            self.device
        )

        self.loss_function = nn.MSELoss()

        self.optimizer = torch.optim.Adam(

            self.model.parameters(),

            lr=learning_rate,

        )

        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(

            self.optimizer,

            mode="min",

            factor=0.5,

            patience=2,

        )

        self.patience = patience

        self.best_loss = float("inf")

        self.early_stop_counter = 0

        self.history = {

            "train_loss": [],

            "validation_loss": [],

        }

    ###########################################################

    def train(

        self,

        train_loader,

        validation_loader,

        epochs=50,

        save_path="app/forecasting/saved_models/revenue_lstm.pt",

    ):

        os.makedirs(

            os.path.dirname(
                save_path
            ),

            exist_ok=True,

        )

        for epoch in range(epochs):

            #########################################

            # TRAIN

            #########################################

            self.model.train()

            train_loss = 0

            for X_batch, y_batch in train_loader:

                X_batch = X_batch.to(
                    self.device
                )

                y_batch = y_batch.to(
                    self.device
                )

                predictions = self.model(
                    X_batch
                ).squeeze()

                loss = self.loss_function(

                    predictions,

                    y_batch,

                )

                self.optimizer.zero_grad()

                loss.backward()

                self.optimizer.step()

                train_loss += loss.item()

            train_loss /= len(train_loader)

            #########################################

            # VALIDATION

            #########################################

            validation_loss = self._validate(
                validation_loader
            )

            #########################################

            # Scheduler

            #########################################

            self.scheduler.step(
                validation_loss
            )

            #########################################

            # History

            #########################################

            self.history[
                "train_loss"
            ].append(
                train_loss
            )

            self.history[
                "validation_loss"
            ].append(
                validation_loss
            )

            #########################################

            # Save Best Model

            #########################################

            if validation_loss < self.best_loss:

                self.best_loss = validation_loss

                self.early_stop_counter = 0

                torch.save(

                    self.model.state_dict(),

                    save_path,

                )

            else:

                self.early_stop_counter += 1

            #########################################

            print(

                f"Epoch "

                f"{epoch+1:02d}"

                f"/{epochs}"

                f" | "

                f"Train: {train_loss:.6f}"

                f" | "

                f"Validation: {validation_loss:.6f}"

            )

            #########################################

            # Early Stopping

            #########################################

            if self.early_stop_counter >= self.patience:

                print()

                print("=" * 60)

                print("Early stopping triggered.")

                print("=" * 60)

                break

        return self.history

    ###########################################################

    def _validate(

        self,

        validation_loader,

    ):

        self.model.eval()

        total_loss = 0

        with torch.no_grad():

            for X_batch, y_batch in validation_loader:

                X_batch = X_batch.to(
                    self.device
                )

                y_batch = y_batch.to(
                    self.device
                )

                outputs = self.model(
                    X_batch
                ).squeeze()

                loss = self.loss_function(

                    outputs,

                    y_batch,

                )

                total_loss += loss.item()

        return total_loss / len(
            validation_loader
        )

    ###########################################################

    def predict(

        self,

        data_loader,

    ):

        self.model.eval()

        predictions = []

        actuals = []

        with torch.no_grad():

            for X_batch, y_batch in data_loader:

                X_batch = X_batch.to(
                    self.device
                )

                outputs = self.model(
                    X_batch
                ).squeeze()

                predictions.extend(

                    outputs.cpu().numpy()

                )

                actuals.extend(

                    y_batch.numpy()

                )

        return (

            predictions,

            actuals,

        )