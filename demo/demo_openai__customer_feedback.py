from dotenv import load_dotenv

load_dotenv()

import os
print(os.getenv("OPENAI_API_KEY"))

from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

from llm_playground.llm.providers.openai import (
    OpenAIProvider,
)

analyst = CustomerFeedbackAnalyst(
    provider=OpenAIProvider(
        api_key=os.getenv("OPENAI_API_KEY")
    )
)

result = analyst.analyze(
    """
    Delivery was delayed by 4 days.
    Customer support never replied.
    Product quality was good.
    """
)

print(result)