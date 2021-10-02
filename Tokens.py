# Tokens.py
# Programmed By Abhinav..
# The File Containing The TokenType Enum And Token Class
# ..

from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    Number = 0
    Add = 1
    Subtract = 2
    Multiply = 3
    Divide = 4
    Mod = 5
    Power = 6
    LeftBracket = 7
    RightBracket = 8

@dataclass
class Token:
    Type: TokenType
    Value: any = None

    def __repr__(Self):
        return Self.Type.name + (f":{Self.Value}" if Self.Value != None else "")
