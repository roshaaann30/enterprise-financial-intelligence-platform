class SchemaValidator:

    @staticmethod
    def validate(dataframe, expected_columns):

        current_columns = set(dataframe.columns)
        expected_columns = set(expected_columns)

        missing_columns = list(
            expected_columns - current_columns
        )

        new_columns = list(
            current_columns - expected_columns
        )

        return {
            "missing_columns": missing_columns,
            "new_columns": new_columns,
            "schema_valid": (
                len(missing_columns) == 0
                and len(new_columns) == 0
            ),
        }