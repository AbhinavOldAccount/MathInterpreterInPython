# Values.py
# Programmed By Abhinav..
# Contains All Different Classes For Number Values
# ..

from dataclasses import dataclass

@dataclass
class Number:
    Value: float

    def __repr__(Self):
        return f"{Self.Value}"