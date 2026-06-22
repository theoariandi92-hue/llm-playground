from llm_playground.customer_feedback.models import (
    Topic,
    Sentiment,
)


def customer_feedback_system_prompt() -> str:

    topics = "\n".join(
        f"- {topic}"
        for topic in Topic.values()
    )

    sentiments = "\n".join(
        f"- {sentiment}"
        for sentiment in Sentiment.values()
    )

    return f"""
You are an experienced customer service analyst.

Classify the feedback into exactly one topic.

Allowed topics:
{topics}

Allowed sentiments:
{sentiments}

Return ONLY valid JSON.

{{
    "topic": "...",
    "sentiment": "...",
    "summary": "..."
}}
"""

CUSTOMER_FEEDBACK_USER_TEMPLATE = """
Analyze the following customer feedback:

{feedback}
"""