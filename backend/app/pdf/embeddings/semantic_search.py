import numpy as np


class SemanticSearch:

    """
    Semantic Search
    """

    @staticmethod
    def search(

        query_embedding,

        embeddings,

        chunks,

        top_k=3,

    ):

        similarities = np.dot(

            embeddings,

            query_embedding,

        )

        indices = (

            np.argsort(

                similarities

            )[::-1][:top_k]

        )

        results = []

        for idx in indices:

            results.append(

                {

                    "chunk":

                        chunks[idx],

                    "score":

                        float(

                            similarities[idx]

                        ),

                }

            )

        return results