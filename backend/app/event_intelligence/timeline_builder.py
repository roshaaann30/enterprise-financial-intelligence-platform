class TimelineBuilder:

    @staticmethod
    def build(

        events,

    ):

        return sorted(

            events,

            key=lambda x:

            x.date,

        )