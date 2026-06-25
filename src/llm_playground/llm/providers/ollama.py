from ollama import chat

from llm_playground.llm.base import (
    BaseLLMProvider,
)


class OllamaProvider(
    BaseLLMProvider,
):

    def __init__(
        self,
        model: str = "qwen2.5:7b",
    ):
        self.model = model

    def generate(
        self,
        messages: list[dict],
    ) -> str:

        response = chat(
            model=self.model,
            messages=messages,
            format="json",
        )

        return response.message.content