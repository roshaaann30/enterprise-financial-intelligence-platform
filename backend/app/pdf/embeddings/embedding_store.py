import numpy as np


class EmbeddingStore:

    """
    Store embeddings
    """

    @staticmethod
    def save(

        embeddings,

        path,

    ):

        np.save(

            path,

            embeddings,

        )

    @staticmethod
    def load(

        path,

    ):

        return np.load(

            path

        )