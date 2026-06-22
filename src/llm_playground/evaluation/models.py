from pydantic import BaseModel


class EvaluationResult(BaseModel):
    topic_accuracy: float
    sentiment_accuracy: float
    average_latency: float
    num_samples: int