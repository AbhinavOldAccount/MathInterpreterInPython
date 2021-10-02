# Reader.py
# Programmed By Abhinav..
# The Program That Describes The Syntax Of The Expression
# ..

from Tokens import TokenType
from Nodes import *

class Parser:
    def __init__(Self, Tokens):
        Self.Tokens = iter(Tokens)
        Self.Advance()

    def ThrowError(Self):
        raise Exception(":Invalid Syntax..")

    def Advance(Self):
        try:
            Self.CurrentToken = next(Self.Tokens)
        except StopIteration:
            Self.CurrentToken = None

    def Parse(Self):
        if Self.CurrentToken == None:
            return None
        Result = Self.Expression()
        if Self.CurrentToken != None:
            Self.ThrowError()
        return Result

    def Expression(Self):
        Result = Self.Term()

        while Self.CurrentToken != None and Self.CurrentToken.Type in (TokenType.Add, TokenType.Subtract):
            if Self.CurrentToken.Type == TokenType.Add:
                Self.Advance()
                Result = AddNode(Result, Self.Term())
            elif Self.CurrentToken.Type == TokenType.Subtract:
                Self.Advance()
                Result = SubtractNode(Result, Self.Term())
            elif Self.CurrentToken.Type == TokenType.Mod:
                Self.Advance()
                Result = ModNode(Result, Self.Term())
        return Result

    def Term(Self):
        Result = Self.Factor()

        while Self.CurrentToken != None and Self.CurrentToken.Type in (TokenType.Multiply, TokenType.Divide, TokenType.Mod, TokenType.Power):
            if Self.CurrentToken.Type == TokenType.Power:
                Self.Advance()
                Result = PowerNode(Result, Self.Factor())
            elif Self.CurrentToken.Type == TokenType.Divide:
                Self.Advance()
                Result = DivideNode(Result, Self.Factor())
            elif Self.CurrentToken.Type == TokenType.Mod:
                Self.Advance()
                Result = ModNode(Result, Self.Factor())
            elif Self.CurrentToken.Type == TokenType.Multiply:
                Self.Advance()
                Result = MultiplyNode(Result, Self.Factor())
        return Result
    
    def Factor(Self):
        Token = Self.CurrentToken
        if Token.Type == TokenType.LeftBracket:
            Self.Advance()
            Result = Self.Expression()
            if Self.CurrentToken.Type != TokenType.RightBracket:
                Self.ThrowError()
            Self.Advance()
            return Result

        elif Token.Type == TokenType.Number:
            Self.Advance()
            return NumberNode(Token.Value)
        elif Token.Type == TokenType.Add:
            Self.Advance()
            return PositiveNode(Self.Factor())
        elif Token.Type == TokenType.Subtract:
            Self.Advance()
            return NegativeNode(Self.Factor())
        Self.ThrowError()