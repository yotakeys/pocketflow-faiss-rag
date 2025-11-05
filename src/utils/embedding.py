"""Utility functions for generating text embeddings using OpenAI's API."""

import numpy as np

from config import config


def get_embedding(text: str):
    """
    Generate an embedding for the given text using OpenAI's API.

    Args:
        text (str): The input text to generate an embedding for.

    Returns:
        list: The embedding vector as a list of floats.
    """

    client = config.openai.client
    response = client.embeddings.create(input=text, model=config.openai.embedding_model)

    embeddings = np.array([d.embedding for d in response.data]).astype("float32")
    return embeddings
