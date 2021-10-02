# Nodes.py
# Programmed By Abhinav..
# The File Containing The Nodes For Numbers And Operations
# ..

from dataclasses import dataclass

@dataclass
class NumberNode:
    Value: float

    def __repr__(Self):
        return f"{Self.Value}"

@dataclass
class AddNode:
    NodeA: any
    NodeB: any

    def __repr__(Self):
        return f"({Self.NodeA}+{Self.NodeB})"

@dataclass
class SubtractNode:
    NodeA: any
    NodeB: any

    def __repr__(Self):
        return f"({Self.NodeA}-{Self.NodeB})"

@dataclass
class MultiplyNode:
    NodeA: any
    NodeB: any

    def __repr__(Self):
        return f"({Self.NodeA}*{Self.NodeB})"


@dataclass
class DivideNode:
    NodeA: any
    NodeB: any

    def __repr__(Self):
        return f"({Self.NodeA}/{Self.NodeB})"

@dataclass
class ModNode:
    NodeA: any
    NodeB: any

    def __repr__(Self):
        return f"({Self.NodeA}%{Self.NodeB})"

@dataclass
class PowerNode:
    NodeA: any
    NodeB: any

    def __repr__(Self):
        return f"({Self.NodeA}^{Self.NodeB})"

@dataclass
class PositiveNode:
    Node: any

    def __repr__(Self):
        return f"(+{Self.Node})"

@dataclass
class NegativeNode:
    Node: any

    def __repr__(Self):
        return f"(-{Self.Node})"