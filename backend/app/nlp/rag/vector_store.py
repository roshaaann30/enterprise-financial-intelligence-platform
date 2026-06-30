import faiss
import numpy as np

from sentence_transformers import (
    SentenceTransformer,
)


class FinancialVectorStore:

    """
    Enterprise Financial Vector Store
    """

    def __init__(

        self,

        model_name=

        "all-MiniLM-L6-v2",

    ):

        self.encoder = (

            SentenceTransformer(

                model_name

            )

        )

        self.index = None

        self.documents = []

    ###########################################################
    # Build Index
    ###########################################################

    def build(

        self,

        chunks,

    ):

        self.documents = chunks

        embeddings = (

            self.encoder.encode(

                chunks,

                convert_to_numpy=True,

            )

        )

        dimension = (

            embeddings.shape[1]

        )

        self.index = (

            faiss.IndexFlatL2(

                dimension

            )

        )

        self.index.add(

            embeddings

        )

    ###########################################################
    # Search
    ###########################################################

    def search(

        self,

        query,

        top_k=5,

    ):

        query_embedding = (

            self.encoder.encode(

                [query],

                convert_to_numpy=True,

            )

        )

        distances, indices = (

            self.index.search(

                query_embedding,

                top_k,

            )

        )

        results = []

        for idx in indices[0]:

            results.append(

                self.documents[idx]

            )

        return results