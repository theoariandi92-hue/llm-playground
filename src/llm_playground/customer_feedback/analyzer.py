from llm_playground.llm.providers.ollama import (
    OllamaProvider,
)

from llm_playground.customer_feedback.prompts import (
    customer_feedback_system_prompt,
    CUSTOMER_FEEDBACK_USER_TEMPLATE,
)

import json

from llm_playground.customer_feedback.models import (
    CustomerFeedbackAnalysis,
)

class CustomerFeedbackAnalyst:

    def __init__(
        self,
        provider=None,
    ):
        self.provider = (
            provider
            or OllamaProvider()
        )

    def analyze(
        self,
        feedback: str,
    ) -> CustomerFeedbackAnalysis:

        messages = [
            {
                "role": "system",
                "content": customer_feedback_system_prompt(),
            },
            {
                "role": "user",
                "content": CUSTOMER_FEEDBACK_USER_TEMPLATE.format(
            feedback=feedback
                ),
            },
        ]

        response = self.provider.generate(
            messages
        )

        data = json.loads(response)

        return CustomerFeedbackAnalysis(
            **data
        )
    
