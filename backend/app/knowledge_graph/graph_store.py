import pickle


class GraphStore:

    @staticmethod
    def save(

        graph,

        path,

    ):

        with open(

            path,

            "wb",

        ) as file:

            pickle.dump(

                graph,

                file,

            )

    @staticmethod
    def load(

        path,

    ):

        with open(

            path,

            "rb",

        ) as file:

            return pickle.load(

                file

            )