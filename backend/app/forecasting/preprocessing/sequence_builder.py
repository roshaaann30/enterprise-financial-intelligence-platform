import numpy as np


class SequenceBuilder:

    @staticmethod
    def build(
        X,
        y,
        sequence_length=20,
    ):

        # Convert pandas objects to numpy if needed
        if hasattr(X, "values"):
            X = X.values

        if hasattr(y, "values"):
            y = y.values

        X_sequences = []

        y_sequences = []

        for i in range(
            sequence_length,
            len(X),
        ):

            X_sequences.append(
                X[
                    i-sequence_length:i
                ]
            )

            y_sequences.append(
                y[i]
            )

        return (

            np.array(
                X_sequences,
                dtype=np.float32,
            ),

            np.array(
                y_sequences,
                dtype=np.float32,
            ),

        )