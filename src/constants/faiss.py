"""Constants for FAISS"""

from enum import Enum
from typing import List
from dataclasses import dataclass

class FaissCategory(str, Enum):
    """Enumeration for different FAISS categories."""
    LINKS = "links"
    DOCUMENTS = "documents"
    IMAGES = "images"
    AUDIO = "audio"

@dataclass
class FaissData:
    """Data class for FAISS data structure."""
    vector: List[float]
    id: int
