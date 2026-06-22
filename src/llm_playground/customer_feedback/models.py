from enum import Enum

from pydantic import BaseModel


class Topic(str, Enum):
    DELIVERY = "Delivery"
    CUSTOMER_SUPPORT = "Customer Support"
    PRODUCT_QUALITY = "Product Quality"
    REFUND = "Refund"
    TECHNICAL_ISSUE = "Technical Issue"
    PRICING = "Pricing"
    OTHERS = "Others"

    @classmethod
    def values(cls) -> list[str]:
        return [topic.value for topic in cls]


class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEUTRAL = "Neutral"
    NEGATIVE = "Negative"

    @classmethod
    def values(cls) -> list[str]:
        return [sentiment.value for sentiment in cls]


class CustomerFeedbackAnalysis(BaseModel):
    topic: Topic
    sentiment: Sentiment
    summary: str