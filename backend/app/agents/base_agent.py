class BaseAgent:

    """
    Base Financial Agent
    """

    def __init__(

        self,

        name,

    ):

        self.name = name

    def run(

        self,

        context,

    ):

        raise NotImplementedError