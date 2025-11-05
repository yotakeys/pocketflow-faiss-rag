"""Configuration for FAISS"""

import os

import faiss

from constants import FaissCategory


class FaissConfig:
    """Configuration class for FAISS"""

    def __init__(self):
        self.dimension = 1536
        self.data_path = os.getenv("DATA_PATH", "./data")
        for category in FaissCategory:
            if os.path.exists(f"{self.data_path}/{category.value}_faiss.index"):
                index = faiss.read_index(
                    f"{self.data_path}/{category.value}_faiss.index"
                )
            else:
                index = faiss.IndexIDMap(faiss.IndexFlatL2(self.dimension))

            setattr(self, f"{category.value}", index)

    def save_index(self, category: FaissCategory):
        """Save the FAISS index for the specified category."""
        index = getattr(self, category.value)
        faiss.write_index(index, f"{self.data_path}/{category.value}_faiss.index")
