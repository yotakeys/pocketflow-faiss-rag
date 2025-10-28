"""Constants for node states in the retrieval flow."""

from enum import Enum

class NodeState(str, Enum):
    """Enumeration for different states of a node."""

    COMMAND = "command"
    ADD = "add"
    SEARCH = "search"
    EXIT = "exit"
