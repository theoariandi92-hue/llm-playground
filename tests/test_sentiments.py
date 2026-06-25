# tests/test_sentiments.py

from llm_playground.customer_feedback.models import (
    Sentiment,
)


def test_sentiment_values():

    assert "Positive" in Sentiment.values()

    assert "Negative" in Sentiment.values()