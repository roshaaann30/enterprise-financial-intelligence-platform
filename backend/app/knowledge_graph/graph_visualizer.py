from pyvis.network import (
    Network,
)


class GraphVisualizer:

    @staticmethod
    def visualize(

        graph,

        output_file=

        "financial_graph.html",

    ):

        net = Network(

            height="800px",

            width="100%",

        )

        net.from_nx(

            graph

        )

        net.save_graph(

            output_file

        )

        return output_file