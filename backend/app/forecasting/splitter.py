class TimeSeriesSplitter:

    @staticmethod
    def split(dataframe):

        n = len(dataframe)

        train_end = int(n * 0.70)

        valid_end = int(n * 0.85)

        train = dataframe.iloc[:train_end]

        validation = dataframe.iloc[
            train_end:valid_end
        ]

        test = dataframe.iloc[
            valid_end:
        ]

        return train, validation, test