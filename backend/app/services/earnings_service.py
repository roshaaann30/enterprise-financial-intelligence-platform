from sqlalchemy.orm import Session

from app.models.earnings_transcript import EarningsTranscript


class EarningsService:

    def __init__(self, db: Session):
        self.db = db

    def save_transcript(self, transcript_data):

        transcript = EarningsTranscript(
            ticker=transcript_data["ticker"],
            fiscal_year=transcript_data["fiscal_year"],
            quarter=transcript_data["quarter"],
            transcript=transcript_data["transcript"],
        )

        self.db.add(transcript)

        self.db.commit()