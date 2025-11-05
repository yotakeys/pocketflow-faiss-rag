"""Configuration for OpenAI API"""

import os

from openai import OpenAI


class OpenAIConfig:
    """Configuration class for OpenAI"""

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        self.client = OpenAI(api_key=api_key)
        self.text_model = "gpt-4o"
        self.embedding_model = "text-embedding-3-small"
