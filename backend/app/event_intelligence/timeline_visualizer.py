import pandas as pd

import plotly.express as px


class TimelineVisualizer:

    @staticmethod
    def visualize(

        timeline,

    ):

        df = pd.DataFrame(

            [

                {

                    "Date":

                        e.date,

                    "Event":

                        e.title,

                    "Impact":

                        e.impact_score,

                }

                for e in timeline

            ]

        )

        fig = px.timeline(

            df,

            x_start="Date",

            x_end="Date",

            y="Event",

        )

        fig.show()