import json


class KnowledgeStore:

    """
    Store knowledge as JSON
    """

    @staticmethod
    def save(

        knowledge,

        path,

    ):

        with open(

            path,

            "w",

            encoding="utf-8",

        ) as file:

            json.dump(

                knowledge,

                file,

                indent=4,

            )

    @staticmethod
    def load(

        path,

    ):

        with open(

            path,

            "r",

            encoding="utf-8",

        ) as file:

            return json.load(

                file

            )