from ollama import chat


class OllamaProvider:

    def __init__(
        self,
        # model: str = "qwen3:8b",
        model: str = "qwen2.5:7b" #better for extraction tasks like classification
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