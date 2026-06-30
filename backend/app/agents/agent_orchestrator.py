class AgentOrchestrator:

    """
    Enterprise Multi-Agent Orchestrator
    """

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

        agents,

    ):

        self.agents = agents

    ###########################################################
    # Run Pipeline
    ###########################################################

    def run(

        self,

        context,

    ):

        pipeline_results = {}

        for agent in self.agents:

            output = agent.run(

                context

            )

            pipeline_results[

                agent.name

            ] = output

            context.update(

                output

            )

        return pipeline_results