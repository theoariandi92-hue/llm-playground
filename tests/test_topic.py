# tests/test_topics.py

from llm_playground.customer_feedback.models import (
    Topic,
)


def test_topic_values():

    assert "Delivery" in Topic.values()

    assert "Refund" in Topic.values()