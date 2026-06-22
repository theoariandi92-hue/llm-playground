# Future use when API credits are available

from dotenv import load_dotenv
load_dotenv()

import os

print(
    os.getenv("OPENAI_API_KEY")[:15]
)

from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

from llm_playground.llm.providers.openai import (
    OpenAIProvider,
)

feedback = """
I ordered a laptop last week.

The delivery arrived 5 days later than promised and
nobody from customer support replied to my emails.

The product itself is working well.
"""

analyst = CustomerFeedbackAnalyst(
    provider=OpenAIProvider()
)

result = analyst.analyze(
    feedback=feedback
)

print(type(result))

print(result.topic)
print(result.sentiment)
print(result.summary)