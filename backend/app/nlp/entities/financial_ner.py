import spacy


class FinancialNER:

    """
    Enterprise Financial NER Engine
    """

    def __init__(

        self,

    ):

        self.nlp = spacy.load(

            "en_core_web_sm"

        )

    ###########################################################
    # Extract Entities
    ###########################################################

    def extract(

        self,

        text,

    ):

        doc = self.nlp(

            text

        )

        entities = []

        for entity in doc.ents:

            entities.append(

                {

                    "text":

                        entity.text,

                    "label":

                        entity.label_,

                }

            )

        return entities