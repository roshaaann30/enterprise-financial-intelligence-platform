from sentence_transformers import (
    SentenceTransformer,
)

import numpy as np


class PDFEmbeddingEngine:

    """
    Enterprise PDF Embedding Engine
    """

    def __init__(

        self,

        model_name=

        "all-MiniLM-L6-v2",

    ):

        self.model = (

            SentenceTransformer(

                model_name

            )

        )

    ###########################################################
    # Embed Chunks
    ###########################################################

    def embed(

        self,

        chunks,

    ):

        embeddings = (

            self.model.encode(

                chunks,

                convert_to_numpy=True,

            )

        )

        return embeddings

    ###########################################################
    # Embed Query
    ###########################################################

    def embed_query(

        self,

        query,

    ):

        return (

            self.model.encode(

                query,

                convert_to_numpy=True,

            )

        )