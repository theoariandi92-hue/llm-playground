# src/llm_playground/llm/providers/openai.py

from openai import OpenAI

from llm_playground.llm.base import (
    BaseLLMProvider,
)


class OpenAIProvider(
    BaseLLMProvider,
):

    def __init__(
        self,
        model: str = "gpt-4.1-mini",
        api_key: str | None = None,
    ):
        self.client = OpenAI(
            api_key=api_key,
        )

        self.model = model

    def generate(
        self,
        messages: list[dict],
    ) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        return response.choices[0].message.content