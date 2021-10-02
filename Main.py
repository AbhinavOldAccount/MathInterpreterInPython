# Main.py
# Programmed By Abhinav..
# The Main File Of The Project
# ..

from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

while True:
    try:
        Text = input(">>: ")
        NewLexer = Lexer(Text)
        Tokens = NewLexer.GenerateTokens()
        NewReader = Parser(Tokens)
        Tree = NewReader.Parse()
        if not Tree:
            continue
        NewInterpreter = Interpreter()
        Value = NewInterpreter.Visit(Tree)
        print(Value)
    except Exception as Error:
        if Error.args[0][0] == ":":
            print(f"Custom: {Error.args[0][1:]}")
        else:
            print(f"Python: {Error}")