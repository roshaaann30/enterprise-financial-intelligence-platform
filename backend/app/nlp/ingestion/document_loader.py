from pathlib import Path

import pandas as pd

from PyPDF2 import PdfReader

from docx import Document

from app.nlp.ingestion.document_types import (
    DocumentType,
)


class FinancialDocumentLoader:

    """
    Enterprise Financial Document Loader
    """

    ###########################################################
    # TXT
    ###########################################################

    @staticmethod
    def load_txt(

        file_path,

    ):

        with open(

            file_path,

            "r",

            encoding="utf-8",

            errors="ignore",

        ) as file:

            return file.read()

    ###########################################################
    # PDF
    ###########################################################

    @staticmethod
    def load_pdf(

        file_path,

    ):

        reader = PdfReader(

            file_path

        )

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted + "\n"

        return text

    ###########################################################
    # DOCX
    ###########################################################

    @staticmethod
    def load_docx(

        file_path,

    ):

        document = Document(

            file_path

        )

        text = []

        for paragraph in document.paragraphs:

            text.append(

                paragraph.text

            )

        return "\n".join(

            text

        )

    ###########################################################
    # CSV
    ###########################################################

    @staticmethod
    def load_csv(

        file_path,

    ):

        df = pd.read_csv(

            file_path

        )

        return df.to_string()

    ###########################################################
    # Detect Type
    ###########################################################

    @staticmethod
    def detect_document_type(

        text,

    ):

        lower = text.lower()

        if (

            "earnings call"

            in lower

        ):

            return DocumentType.EARNINGS_CALL

        if (

            "annual report"

            in lower

        ):

            return DocumentType.ANNUAL_REPORT

        if (

            "quarterly report"

            in lower

        ):

            return DocumentType.QUARTERLY_REPORT

        if (

            "dear shareholders"

            in lower

        ):

            return DocumentType.CEO_LETTER

        if (

            "investor presentation"

            in lower

        ):

            return DocumentType.INVESTOR_PRESENTATION

        return DocumentType.UNKNOWN

    ###########################################################
    # Generic Load
    ###########################################################

    @staticmethod
    def load(

        file_path,

    ):

        path = Path(

            file_path

        )

        suffix = (

            path.suffix.lower()

        )

        if suffix == ".txt":

            text = (

                FinancialDocumentLoader.load_txt(

                    file_path

                )

            )

        elif suffix == ".pdf":

            text = (

                FinancialDocumentLoader.load_pdf(

                    file_path

                )

            )

        elif suffix == ".docx":

            text = (

                FinancialDocumentLoader.load_docx(

                    file_path

                )

            )

        elif suffix == ".csv":

            text = (

                FinancialDocumentLoader.load_csv(

                    file_path

                )

            )

        else:

            raise ValueError(

                f"Unsupported file type: {suffix}"

            )

        document_type = (

            FinancialDocumentLoader.detect_document_type(

                text

            )

        )

        return {

            "text": text,

            "document_type": document_type.value,

            "file_name": path.name,

            "file_path": str(path),

        }