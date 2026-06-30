class FinancialGraphSearch:

    @staticmethod
    def find_relationships(

        graph,

        node,

    ):

        relationships = []

        for neighbor in graph.neighbors(

            node

        ):

            edge = graph.get_edge_data(

                node,

                neighbor,

            )

            relationships.append(

                {

                    "target":

                        neighbor,

                    "relationship":

                        edge.get(

                            "relationship"

                        ),

                }

            )

        return relationships