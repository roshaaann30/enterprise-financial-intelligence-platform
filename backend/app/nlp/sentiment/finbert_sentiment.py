import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
)


class FinBERTSentiment:

    """
    Financial Sentiment Analysis
    """

    MODEL_NAME = (

        "ProsusAI/finbert"

    )

    LABELS = {

        0: "Positive",

        1: "Negative",

        2: "Neutral",

    }

    ###########################################################
    # Constructor
    ###########################################################

    def __init__(

        self,

    ):

        self.tokenizer = (

            AutoTokenizer.from_pretrained(

                self.MODEL_NAME

            )

        )

        self.model = (

            AutoModelForSequenceClassification.from_pretrained(

                self.MODEL_NAME

            )

        )

    ###########################################################
    # Predict
    ###########################################################

    def predict(

        self,

        text,

    ):

        inputs = self.tokenizer(

            text,

            return_tensors="pt",

            truncation=True,

            max_length=512,

        )

        with torch.no_grad():

            outputs = self.model(

                **inputs

            )

        probabilities = (

            torch.softmax(

                outputs.logits,

                dim=1,

            )

            .cpu()

            .numpy()[0]

        )

        prediction = int(

            probabilities.argmax()

        )

        confidence = float(

            probabilities.max()

        )

        return {

            "sentiment":

                self.LABELS[

                    prediction

                ],

            "confidence":

                round(

                    confidence * 100,

                    2,

                ),

            "probabilities": {

                "positive":

                    round(

                        probabilities[0] * 100,

                        2,

                    ),

                "negative":

                    round(

                        probabilities[1] * 100,

                        2,

                    ),

                "neutral":

                    round(

                        probabilities[2] * 100,

                        2,

                    ),

            },

        }