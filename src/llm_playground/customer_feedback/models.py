from pydantic import BaseModel

class CustomerFeedbackAnalysis(BaseModel):
    topic: str
    sentiment: str
    summary: str