"""Node to handle ADD command interactions with the system"""

from pocketflow import Node
from constants import NodeState
from utils import add_index, add_data, get_embedding
from random import randint


class AddNode(Node):
    """Node to handle ADD command interactions with the system."""
    def prep(self, shared: dict):
        return shared["commands"]

    def exec(self, prep_res: dict | NodeState):
        if prep_res == NodeState.EXIT:
            return NodeState.EXIT

        category = prep_res["category"][0]
        description = " ".join(prep_res["description"])
        id_data = randint(1000, 9999)

        new_data = {
            "id": id_data,
            "category": category,
            "description": description
        }
        print(f"Adding data: {new_data}")
        add_data(new_data)

        embedding = get_embedding(description)
        new_data["vector"] = embedding
        add_index(category, new_data)
        print(f"\nData added with ID: {id_data}")
        return NodeState.COMMAND


    def post(self, shared: dict, prep_res: dict, exec_res: NodeState):
        return exec_res
