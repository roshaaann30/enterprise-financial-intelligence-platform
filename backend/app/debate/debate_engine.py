from app.debate.bull_analyst import (
    BullAnalyst,
)

from app.debate.bear_analyst import (
    BearAnalyst,
)


class DebateEngine:

    """
    AI Debate Engine
    """

    @staticmethod
    def run(

        context,

    ):

        bull = (

            BullAnalyst.analyze(

                context

            )

        )

        bear = (

            BearAnalyst.analyze(

                context

            )

        )

        return {

            "bull_case":

                bull,

            "bear_case":

                bear,

        }