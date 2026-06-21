from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)


feedback = """
I ordered a laptop last week.

The delivery arrived 5 days later than promised and
nobody from customer support replied to my emails.

The product itself is working well.
"""


analyst = CustomerFeedbackAnalyst()

result = analyst.analyze(
    feedback=feedback
)

print(result)