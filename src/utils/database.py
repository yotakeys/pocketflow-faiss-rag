"""Utility functions for database operations."""

from config import config
from constants.database import DataObject
from constants.faiss import FaissCategory

def add_data(new_data: DataObject):
    """
    add data to the database for the specified category.

    Args:
        new_data (dict): The data to be added.
    """
    data = config.database.data
    if new_data['category'] not in data:
        data[new_data['category']] = []

    data[new_data['category']].append({
        "id": new_data['id'],
        "description": new_data['description'],
    })

def get_data(category: FaissCategory, data_id: int):
    """
    Retrieve data from the database for the specified category.

    Args:
        category (FaissCategory): The category of the data to retrieve.
        data_id (int): The ID of the data to retrieve.

    Returns:
        dict: The retrieved data, or None if not found.
    """
    data = config.database.data
    return next((item for item in data.get(category, []) if item["id"] == data_id), None)
