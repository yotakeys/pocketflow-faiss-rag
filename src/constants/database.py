"""Constants for database objects."""

from dataclasses import dataclass
from .faiss import FaissCategory

@dataclass
class DataObject:
    """Data class for database object structure."""
    id: int
    category: FaissCategory
    content: dict
    description: str
