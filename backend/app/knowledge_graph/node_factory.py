from app.knowledge_graph.graph_schema import (
    GraphNode,
)

from app.knowledge_graph.entity_types import (
    EntityType,
)


class NodeFactory:

    @staticmethod
    def create(

        node_id,

        entity_type,

        properties=None,

    ):

        return GraphNode(

            node_id=node_id,

            node_type=entity_type.value,

            properties=properties,

        )