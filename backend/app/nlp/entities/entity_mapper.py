class FinancialEntityMapper:

    MAPPING = {

        "ORG": "Organization",

        "PERSON": "Executive",

        "MONEY": "Financial Metric",

        "GPE": "Country",

        "LOC": "Region",

        "PRODUCT": "Product",

    }

    @classmethod
    def map(

        cls,

        entities,

    ):

        results = []

        for entity in entities:

            results.append(

                {

                    "entity":

                        entity["text"],

                    "category":

                        cls.MAPPING.get(

                            entity["label"],

                            entity["label"],

                        ),

                }

            )

        return results