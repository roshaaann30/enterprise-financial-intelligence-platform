class RelationshipExtractor:

    @staticmethod
    def extract(

        knowledge,

    ):

        edges = []

        company = (

            knowledge.get(

                "company"

            )

        )

        ###################################################
        # Competitors
        ###################################################

        for competitor in knowledge.get(

            "competitors",

            [],

        ):

            edges.append(

                (

                    company,

                    competitor,

                    "COMPETES_WITH",

                )

            )

        ###################################################
        # Products
        ###################################################

        for product in knowledge.get(

            "products",

            [],

        ):

            edges.append(

                (

                    company,

                    product,

                    "PRODUCES",

                )

            )

        return edges