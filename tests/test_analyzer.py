# tests/test_analyzer.py

from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

from llm_playground.llm.providers.mock import (
    MockProvider,
)


def test_analyzer():

    analyst = CustomerFeedbackAnalyst(
        provider=MockProvider()
    )

    result = analyst.analyze(
        "My package is late"
    )

    assert result.topic.value == "Delivery"

    assert result.sentiment.value == "Negative"