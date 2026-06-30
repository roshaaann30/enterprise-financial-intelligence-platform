import re

from typing import List


class FinancialTextPreprocessor:

    """
    Enterprise Financial Text Preprocessor
    """

    ###########################################################
    # Lowercase
    ###########################################################

    @staticmethod
    def lowercase(

        text: str,

    ) -> str:

        return text.lower()

    ###########################################################
    # Remove URLs
    ###########################################################

    @staticmethod
    def remove_urls(

        text: str,

    ) -> str:

        return re.sub(

            r"https?://\S+|www\.\S+",

            "",

            text,

        )

    ###########################################################
    # Remove Emails
    ###########################################################

    @staticmethod
    def remove_emails(

        text: str,

    ) -> str:

        return re.sub(

            r"\S+@\S+",

            "",

            text,

        )

    ###########################################################
    # Preserve Financial Symbols
    ###########################################################

    @staticmethod
    def preserve_financial_terms(

        text: str,

    ) -> str:

        replacements = {

            "$": " USD ",

            "%": " PERCENT ",

            "AI": " AI ",

            "ESG": " ESG ",

            "IPO": " IPO ",

            "EBITDA": " EBITDA ",

        }

        for old, new in replacements.items():

            text = text.replace(

                old,

                new,

            )

        return text

    ###########################################################
    # Remove Special Characters
    ###########################################################

    @staticmethod
    def remove_special_characters(

        text: str,

    ) -> str:

        return re.sub(

            r"[^a-zA-Z0-9\s\.\,\-\%]",

            " ",

            text,

        )

    ###########################################################
    # Remove Extra Spaces
    ###########################################################

    @staticmethod
    def normalize_spaces(

        text: str,

    ) -> str:

        return re.sub(

            r"\s+",

            " ",

            text,

        ).strip()

    ###########################################################
    # Sentence Split
    ###########################################################

    @staticmethod
    def split_sentences(

        text: str,

    ) -> List[str]:

        return re.split(

            r"(?<=[.!?])\s+",

            text,

        )

    ###########################################################
    # Full Pipeline
    ###########################################################

    @staticmethod
    def process(

        text: str,

    ) -> str:

        text = FinancialTextPreprocessor.remove_urls(

            text

        )

        text = FinancialTextPreprocessor.remove_emails(

            text

        )

        text = FinancialTextPreprocessor.preserve_financial_terms(

            text

        )

        text = FinancialTextPreprocessor.lowercase(

            text

        )

        text = FinancialTextPreprocessor.remove_special_characters(

            text

        )

        text = FinancialTextPreprocessor.normalize_spaces(

            text

        )

        return text