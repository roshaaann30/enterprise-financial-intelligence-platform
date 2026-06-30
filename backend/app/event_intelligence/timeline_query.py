class TimelineQuery:

    @staticmethod
    def filter_by_type(

        timeline,

        event_type,

    ):

        return [

            event

            for event in timeline

            if event.event_type

            == event_type

        ]