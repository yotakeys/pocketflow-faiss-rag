"""Constants for FAISS"""

from dataclasses import dataclass
from enum import Enum
from typing import List


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
