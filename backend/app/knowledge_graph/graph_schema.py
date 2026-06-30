class GraphNode:

    def __init__(

        self,

        node_id,

        node_type,

        properties=None,

    ):

        self.node_id = node_id

        self.node_type = node_type

        self.properties = (

            properties or {}

        )


class GraphEdge:

    def __init__(

        self,

        source,

        target,

        relationship,

    ):

        self.source = source

        self.target = target

        self.relationship = relationship