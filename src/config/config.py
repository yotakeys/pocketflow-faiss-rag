"""Configuration module for the application."""

from .database import DatabaseConfig
from .faiss import FaissConfig
from .openai import OpenAIConfig


class Config:
    """Main configuration class for the application."""

    def __init__(self):
        self.openai = OpenAIConfig()
        self.faiss = FaissConfig()
        self.database = DatabaseConfig()


config = Config()
