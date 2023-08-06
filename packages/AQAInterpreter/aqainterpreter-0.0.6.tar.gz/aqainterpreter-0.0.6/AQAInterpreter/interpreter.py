from AQAInterpreter.tokens import *
from AQAInterpreter.scanner import *
from AQAInterpreter.errors import *
from AQAInterpreter.environment import SymbolTable
from abc import abstractmethod

environment = SymbolTable()


class Expr:
    @abstractmethod
    def interpret(self) -> object:
        ...


class Stmt:
    @abstractmethod
    def interpret(self, output: list[str]) -> object:
        ...


@dataclass
class Literal(Expr):
    value: object

    def interpret(self):
        return self.value


@dataclass
class Logical(Expr):
    left: Expr
    operator: Token
    right: Expr

    def interpret(self):
        left = self.left.interpret()
        right = self.right.interpret()

        if self.operator.type == OR:
            if left:
                return left
        else:
            # operator is AND
            if not left:
                return left

        return right


@dataclass
class Unary(Expr):
    operator: Token
    right: Expr

    def interpret(self) -> object:
        if (type := self.operator.type) == MINUS:
            return -self.right.interpret()  # type: ignore
        elif type == NOT:
            return not self.right.interpret()


@dataclass
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

    def interpret(self) -> object:
        left = self.left.interpret()
        right = self.right.interpret()

        if (token_type := self.operator.type) == ADD:
            if (type(left), type(right)) in {(str, int), (int, str)}:
                return str(left) + str(right)
            else:
                return left + right  # type: ignore
        elif token_type == MINUS:
            return left - right  # type: ignore
        elif token_type == TIMES:
            return left * right  # type: ignore
        elif token_type == DIVIDE:
            return left / right  # type: ignore
        elif token_type == GREATER:
            return left > right  # type: ignore
        elif token_type == GREATER_EQUAL:
            return left >= right  # type: ignore
        elif token_type == LESS:
            return left < right  # type: ignore
        elif token_type == LESS_EQUAL:
            return left <= right  # type: ignore
        elif token_type == EQUAL:
            return left == right
        elif token_type == NOT_EQUAL:
            return left != right


@dataclass
class Grouping(Expr):
    expression: Expr

    def interpret(self):
        return self.expression.interpret()


@dataclass
class Variable(Expr):
    name: Token

    def interpret(self) -> object:
        return environment.get(self.name)


@dataclass
class Print(Stmt):
    expression: Expr

    def interpret(self, output: list[str]):
        output.append(str(self.expression.interpret()) + "\n")


@dataclass
class While(Stmt):
    condition: Expr
    body: list[Stmt]

    def interpret(self, output: list[str]) -> object:
        while self.condition.interpret():
            for stmt in self.body:
                stmt.interpret(output)


@dataclass
class If(Stmt):
    condition: Expr
    then_branch: list[Stmt]
    else_branch: list[Stmt]

    def interpret(self, output: list[str]):
        if self.condition.interpret():
            for stmt in self.then_branch:
                stmt.interpret(output)

        else:
            for stmt in self.else_branch:
                stmt.interpret(output)


@dataclass
class Var(Stmt):
    name: Token
    initialiser: Expr

    def interpret(self, output: list[str]):
        value = self.initialiser.interpret()
        environment.define(self.name.lexeme, value)
