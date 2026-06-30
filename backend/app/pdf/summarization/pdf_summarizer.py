class PDFSummarizer:

    """
    Enterprise PDF Summarizer
    """

    ###########################################################
    # Executive Summary
    ###########################################################

    @staticmethod
    def summarize(

        text,

        max_length=2000,

    ):

        text = text.strip()

        if len(text) <= max_length:

            return text

        return (

            text[:max_length]

            + "\n\n[Summary Truncated]"

        )