class MockProvider:

    def generate(
        self,
        messages,
    ) -> str:

        return """
        {
            "topic": "Delivery",
            "sentiment": "Negative",
            "summary": "Package arrived late"
        }
        """