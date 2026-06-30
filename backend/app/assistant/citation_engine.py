class CitationEngine:

    """
    Citation Generator
    """

    @staticmethod
    def build(

        retrieved_chunks,

    ):

        citations = []

        for idx, chunk in enumerate(

            retrieved_chunks,

            start=1,

        ):

            citations.append(

                {

                    "source":

                        f"Document Chunk {idx}",

                    "text":

                        chunk,

                }

            )

        return citations