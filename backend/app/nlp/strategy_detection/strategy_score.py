class StrategicScore:

    @staticmethod
    def calculate(

        initiatives,

    ):

        score = 0

        for item in initiatives:

            priority = item["priority"]

            if priority == "High":

                score += 15

            elif priority == "Medium":

                score += 10

            else:

                score += 5

        return min(

            score,

            100,

        )