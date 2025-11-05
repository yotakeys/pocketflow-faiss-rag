"""Configuration for JSON Database"""

import json
import os

from constants.database import DataObject


class DatabaseConfig:
    """Configuration class for Database connections."""

    def __init__(self):
        self.data_path = os.getenv("DATA_PATH", "./data")
        self.db_file = os.path.join(self.data_path, "database.json")

        if not os.path.exists(self.db_file):
            with open(self.db_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

        self.data: DataObject = self.load_data()

    def load_data(self):
        """Load data from the JSON database file."""
        with open(self.db_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_data(self):
        """Save data to the JSON database file."""
        with open(self.db_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
