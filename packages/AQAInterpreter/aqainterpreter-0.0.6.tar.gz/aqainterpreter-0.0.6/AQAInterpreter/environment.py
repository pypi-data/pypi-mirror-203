from dataclasses import dataclass, field

from AQAInterpreter.errors import *


@dataclass
class SymbolTable:
    """symbol table used to track state of varaibles"""

    values: dict[str, object] = field(default_factory=dict)

    def get(self, name: Token) -> object:
        """returns `name` from symbol table if it exists"""
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        raise AQARuntimeError(name, f"undefined variable '{name.lexeme}'")

    def define(self, name: str, value: object) -> None:
        """assigns `value` to symbol table"""
        self.values[name] = value
