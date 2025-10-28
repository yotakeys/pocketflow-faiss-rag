"""Utility functions for FAISS operations."""

from config import config
from constants import FaissCategory, FaissData
import numpy as np

def add_index(category: FaissCategory, data: FaissData):
    """
    Add an index to the FAISS index for the specified category.

    Args:
        category (FaissCategory): The category of the FAISS index.
        data (FaissData): The data containing vectors and their IDs.
    """
    index = getattr(config.faiss, category)
    index.add_with_ids(data["vector"], np.array([data["id"]], dtype="int64"))

def search_index(category: FaissCategory, query_vector, top_k=5):
    """
    Search the FAISS index for the specified category.

    Args:
        category (FaissCategory): The category of the FAISS index.
        query_vector (list): The query vector to search.
        top_k (int): The number of top results to return.
    Returns:
        tuple: Distances and indices of the top_k nearest neighbors.
    """
    index = getattr(config.faiss, category)
    _, ids = index.search(query_vector, top_k)
    return ids[0]
