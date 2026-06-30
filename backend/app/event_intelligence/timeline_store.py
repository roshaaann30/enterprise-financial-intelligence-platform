import json


class TimelineStore:

    @staticmethod
    def save(

        timeline,

        path,

    ):

        with open(

            path,

            "w",

            encoding="utf-8",

        ) as file:

            json.dump(

                [

                    vars(event)

                    for event in timeline

                ],

                file,

                indent=4,

            )