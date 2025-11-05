"""Flow for handling interactions."""

from pocketflow import Flow

from constants import NodeState
from nodes import AddNode, CommandNode, ExitNode, SearchNode


class FlowChat(Flow):
    """Flow for handling interactions."""

    def __init__(self):
        command_node = CommandNode()
        exit_node = ExitNode()
        add_node = AddNode()
        search_node = SearchNode()

        command_node - NodeState.EXIT >> exit_node
        command_node - NodeState.ADD >> add_node
        command_node - NodeState.SEARCH >> search_node
        add_node - NodeState.COMMAND >> command_node
        search_node - NodeState.COMMAND >> command_node

        super().__init__(start=command_node)
