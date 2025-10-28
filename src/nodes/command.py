"""Node to handle chat interactions with the system"""

from pocketflow import Node
from constants import NodeState


class CommandNode(Node):
    """Node to handle chat interactions with the system."""
    def prep(self, shared: dict):
        user_input = input("\nCOMMAND DESCRIPTION: ")

        if user_input.lower() == 'exit':
            return NodeState.EXIT
        user_input = user_input.strip().split()
        shared["commands"] = {
            "command": user_input[0],
            "category": user_input[1:2],
            "description": user_input[2:],
        }
        return shared["commands"]

    def exec(self, prep_res: dict | NodeState):
        if prep_res == NodeState.EXIT:
            return NodeState.EXIT
        elif prep_res["command"] == "add":
            return NodeState.ADD
        elif prep_res["command"] == "search":
            return NodeState.SEARCH
        else:
            return NodeState.EXIT

    def post(self, shared: dict, prep_res: dict, exec_res: NodeState):
        if exec_res == NodeState.EXIT:
            print("\nGoodbye!")
            return NodeState.EXIT 

        return exec_res
