# api/models.py

from pydantic import BaseModel


class AnalyzeFeedbackRequest(
    BaseModel
):
    feedback: str