from app.agents.base_agent import (
    BaseAgent,
)

from app.agents.agent_orchestrator import (
    AgentOrchestrator,
)


class TestAgent(

    BaseAgent

):

    def run(

        self,

        context,

    ):

        return {

            "message":

                f"Hello from {self.name}"

        }


agents = [

    TestAgent(

        "Agent1"

    ),

    TestAgent(

        "Agent2"

    ),

]

orchestrator = (

    AgentOrchestrator(

        agents

    )

)

result = (

    orchestrator.run(

        {}

    )

)

print(result)