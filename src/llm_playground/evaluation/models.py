from pydantic import BaseModel


class EvaluationResult(BaseModel):
    model_name: str
    topic_accuracy: float
    sentiment_accuracy: float
    average_latency: float

    num_samples: int
    successful_predictions: int
    failed_predictions: int
    success_rate: float