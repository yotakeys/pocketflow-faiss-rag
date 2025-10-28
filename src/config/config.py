"""Configuration module for the application."""

from .faiss import FaissConfig
from .openai import OpenAIConfig
from .database import DatabaseConfig

class Config:
    """Main configuration class for the application."""
    def __init__(self):
        self.openai = OpenAIConfig()
        self.faiss = FaissConfig()
        self.database = DatabaseConfig()

config = Config()
