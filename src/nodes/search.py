"""Node to handle ADD command interactions with the system"""

from pocketflow import Node

from constants import NodeState
from utils import get_data, get_embedding, search_index


class SearchNode(Node):
    """Node to handle SEARCH command interactions with the system."""

    def prep(self, shared: dict):
        return shared["commands"]

    def exec(self, prep_res: dict | NodeState):
        if prep_res == NodeState.EXIT:
            return NodeState.EXIT

        category = prep_res["category"][0]
        description = " ".join(prep_res["description"])

        embedding = get_embedding(description)
        results = search_index(category, embedding, top_k=5)
        print("\nSearch Results:")
        for result in results:
            if result == -1:
                continue
            data = get_data(category, result)
            print(f"ID: {data['id']}, " f"Description: {data['description']}, ")

        return NodeState.COMMAND

    def post(self, shared: dict, prep_res: dict, exec_res: NodeState):
        return exec_res
