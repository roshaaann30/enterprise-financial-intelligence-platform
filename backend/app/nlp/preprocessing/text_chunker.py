import re


class FinancialTextChunker:

    """
    Enterprise Financial Text Chunker
    """

    ###########################################################
    # Clean Text
    ###########################################################

    @staticmethod
    def clean(

        text,

    ):

        text = re.sub(

            r"\s+",

            " ",

            text,

        )

        return text.strip()

    ###########################################################
    # Fixed Size Chunks
    ###########################################################

    @staticmethod
    def chunk_by_words(

        text,

        chunk_size=300,

        overlap=50,

    ):

        text = FinancialTextChunker.clean(

            text

        )

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = start + chunk_size

            chunk = " ".join(

                words[start:end]

            )

            chunks.append(

                chunk

            )

            start += (

                chunk_size - overlap

            )

        return chunks

    ###########################################################
    # Paragraph Chunks
    ###########################################################

    @staticmethod
    def chunk_by_paragraph(

        text,

    ):

        paragraphs = [

            p.strip()

            for p in text.split("\n")

            if p.strip()

        ]

        return paragraphs

    ###########################################################
    # Sentence Chunks
    ###########################################################

    @staticmethod
    def chunk_by_sentence(

        text,

        max_sentences=5,

    ):

        sentences = re.split(

            r"(?<=[.!?])\s+",

            text,

        )

        chunks = []

        for i in range(

            0,

            len(sentences),

            max_sentences,

        ):

            chunk = " ".join(

                sentences[i:i + max_sentences]

            )

            chunks.append(

                chunk

            )

        return chunks

    ###########################################################
    # Metadata
    ###########################################################

    @staticmethod
    def add_metadata(

        chunks,

        source_file,

        document_type,

    ):

        results = []

        for index, chunk in enumerate(

            chunks

        ):

            results.append(

                {

                    "chunk_id":

                        index,

                    "text":

                        chunk,

                    "source":

                        source_file,

                    "document_type":

                        document_type,

                }

            )

        return results

    ###########################################################
    # Full Pipeline
    ###########################################################

    @staticmethod
    def process(

        text,

        source_file,

        document_type,

        chunk_size=300,

        overlap=50,

    ):

        chunks = (

            FinancialTextChunker.chunk_by_words(

                text,

                chunk_size,

                overlap,

            )

        )

        return (

            FinancialTextChunker.add_metadata(

                chunks,

                source_file,

                document_type,

            )

        )