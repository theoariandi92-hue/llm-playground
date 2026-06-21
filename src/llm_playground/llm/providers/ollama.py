from ollama import chat


class OllamaProvider:

    def __init__(
        self,
        model: str = "qwen3:8b",
    ):
        self.model = model

    def generate(
        self,
        messages: list[dict],
    ) -> str:

        response = chat(
            model=self.model,
            messages=messages,
        )

        return response.message.content