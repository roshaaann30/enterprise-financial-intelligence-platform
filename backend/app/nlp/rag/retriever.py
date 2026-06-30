class FinancialRetriever:

    @staticmethod
    def retrieve(

        vector_store,

        query,

        top_k=5,

    ):

        return (

            vector_store.search(

                query,

                top_k,

            )

        )