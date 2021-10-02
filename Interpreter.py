# Interpreter.py
# Programmed By Abhinav..
# The Program That Gives The Result Of The Expression
# ..

from Nodes import *
from Values import Number

class Interpreter:
    def Visit(Self, Node):
        FunctionName = f"Visit_{type(Node).__name__}"
        Function = getattr(Self, FunctionName)
        return Function(Node)

    def Visit_NumberNode(Self, Node):
        return Number(Node.Value)

    def Visit_AddNode(Self, Node):
        return Number(Self.Visit(Node.NodeA).Value + Self.Visit(Node.NodeB).Value)

    def Visit_SubtractNode(Self, Node):
        return Number(Self.Visit(Node.NodeA).Value - Self.Visit(Node.NodeB).Value)

    def Visit_MultiplyNode(Self, Node):
        return Number(Self.Visit(Node.NodeA).Value * Self.Visit(Node.NodeB).Value)

    def Visit_DivideNode(Self, Node):
        try:
            return Number(Self.Visit(Node.NodeA).Value / Self.Visit(Node.NodeB).Value)
        except:
            raise Exception(":Math Error..")

    def Visit_ModNode(Self, Node):
        try:
            return Number(Self.Visit(Node.NodeA).Value % Self.Visit(Node.NodeB).Value)
        except:
            raise Exception(":Math Error..")

    def Visit_PowerNode(Self, Node):
        return Number(Self.Visit(Node.NodeA).Value ** Self.Visit(Node.NodeB).Value)

    def Visit_PositiveNode(Self, Node):
        return Self.Visit(Node.Node)
    
    def Visit_NegativeNode(Self, Node):
        return Number(-Self.Visit(Node.Node).Value)