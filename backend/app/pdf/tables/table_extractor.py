import pdfplumber

import pandas as pd


class FinancialTableExtractor:

    """
    Enterprise Financial Table Extractor
    """

    ###########################################################
    # Extract Tables
    ###########################################################

    @staticmethod
    def extract(

        pdf_path,

    ):

        tables = []

        with pdfplumber.open(

            pdf_path

        ) as pdf:

            for page_number, page in enumerate(

                pdf.pages,

                start=1,

            ):

                extracted_tables = (

                    page.extract_tables()

                )

                for table_index, table in enumerate(

                    extracted_tables,

                    start=1,

                ):

                    try:

                        df = pd.DataFrame(

                            table

                        )

                        tables.append(

                            {

                                "page":

                                    page_number,

                                "table":

                                    table_index,

                                "data":

                                    df,

                            }

                        )

                    except Exception:

                        pass

        return tables