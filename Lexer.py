# Lexer.py
# Programmed By Abhinav..
# The Program That Splits The Expression Into Tokens
# ..


from Tokens import Token, TokenType

Digits = "0123456789"

class Lexer:
    def __init__(Self, Text):
        Self.Text = iter(Text)
        Self.Advance()

    def Advance(Self):
        try:
            Self.CurrentCharacter = next(Self.Text)
        except StopIteration:
            Self.CurrentCharacter = None

    def GenerateTokens(Self):
        while Self.CurrentCharacter != None:
            if Self.CurrentCharacter == " ":
                Self.Advance()
            elif Self.CurrentCharacter == "." or Self.CurrentCharacter in Digits:
                yield Self.GenerateNumber()
            elif Self.CurrentCharacter == "+":
                Self.Advance()
                yield Token(TokenType.Add)
            elif Self.CurrentCharacter == "-":
                Self.Advance()
                yield Token(TokenType.Subtract)
            elif Self.CurrentCharacter == "*":
                Self.Advance()
                yield Token(TokenType.Multiply)
            elif Self.CurrentCharacter == "/":
                Self.Advance()
                yield Token(TokenType.Divide)
            elif Self.CurrentCharacter == "%":
                Self.Advance()
                yield Token(TokenType.Mod)
            elif Self.CurrentCharacter == "^":
                Self.Advance()
                yield Token(TokenType.Power)
            elif Self.CurrentCharacter == "(":
                Self.Advance()
                yield Token(TokenType.LeftBracket)
            elif Self.CurrentCharacter == ")":
                Self.Advance()
                yield Token(TokenType.RightBracket)
            else:
                raise Exception(f':Illegal Character "{Self.CurrentCharacter}"..')

    def GenerateNumber(Self):
        DecimalPointCount = 0
        NumberString = Self.CurrentCharacter
        Self.Advance()

        while Self.CurrentCharacter != None and (Self.CurrentCharacter == "." or Self.CurrentCharacter in Digits):
            if Self.CurrentCharacter == ".":
                if DecimalPointCount > 1:
                    break

            NumberString += Self.CurrentCharacter
            Self.Advance()
        
        if NumberString[0] == ".":
            NumberString = "0" + NumberString
        
        if NumberString[-1] == ".":
            NumberString = 0 + NumberString

        return Token(TokenType.Number, float(NumberString))