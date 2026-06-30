class OutlookScore:

    SCORES = {

        "Very Positive": 100,

        "Positive": 80,

        "Neutral": 60,

        "Negative": 40,

        "Very Negative": 20,

    }

    @classmethod
    def calculate(

        cls,

        outlook,

    ):

        return cls.SCORES.get(

            outlook,

            60,

        )