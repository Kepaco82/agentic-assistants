import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


class LLMClient:
    def __init__(
        self,
        client: Any | None = None,
        model: str = "gpt-5.1",
    ):
        load_dotenv()

        self.model = model

        if client is not None:
            self.client = client
            return

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is not configured."
            )

        self.client = OpenAI(api_key=api_key)

    def generate(
        self,
        instructions: str,
        input_text: str,
    ) -> dict[str, str | None]:
        response = self.client.responses.create(
            model=self.model,
            instructions=instructions,
            input=input_text,
        )

        return {
            "text": response.output_text,
            "request_id": getattr(
                response,
                "_request_id",
                None,
            ),
        }