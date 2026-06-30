from pathlib import Path

import fitz


class PDFExtractor:

    """
    Enterprise PDF Extraction Engine
    """

    ###########################################################
    # Extract PDF
    ###########################################################

    @staticmethod
    def extract(

        file_path,

    ):

        pdf = fitz.open(

            file_path

        )

        pages = []

        full_text = ""

        #######################################################
        # Pages
        #######################################################

        for page_number in range(

            len(pdf)

        ):

            page = pdf.load_page(

                page_number

            )

            text = page.get_text()

            full_text += text + "\n"

            pages.append(

                {

                    "page_number":

                        page_number + 1,

                    "text":

                        text,

                }

            )

        #######################################################
        # Metadata
        #######################################################

        metadata = pdf.metadata

        #######################################################
        # Output
        #######################################################

        return {

            "file_name":

                Path(

                    file_path

                ).name,

            "page_count":

                len(

                    pdf

                ),

            "metadata":

                metadata,

            "text":

                full_text,

            "pages":

                pages,

        }