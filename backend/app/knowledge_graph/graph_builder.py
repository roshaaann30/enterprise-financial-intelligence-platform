import networkx as nx


class FinancialGraphBuilder:

    @staticmethod
    def build(

        knowledge,

        edges,

    ):

        graph = nx.Graph()

        company = (

            knowledge["company"]

        )

        graph.add_node(

            company,

            type="Company",

        )

        for source, target, relation in edges:

            graph.add_node(

                target

            )

            graph.add_edge(

                source,

                target,

                relationship=relation,

            )

        return graph