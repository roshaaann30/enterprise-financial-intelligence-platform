from app.knowledge_graph.node_factory import (
    NodeFactory,
)

from app.knowledge_graph.entity_types import (
    EntityType,
)

node = (

    NodeFactory.create(

        "Apple",

        EntityType.COMPANY,

        {

            "ticker":

                "AAPL"

        }

    )

)

print(

    node.node_id

)

print(

    node.node_type

)

print(

    node.properties

)