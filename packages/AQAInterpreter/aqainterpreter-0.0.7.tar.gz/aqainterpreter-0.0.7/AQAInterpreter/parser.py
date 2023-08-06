from AQAInterpreter.interpreter import *
from AQAInterpreter import errors


@dataclass
class Parser:
    tokens: list[Token]
    _current: int = 0

    def _error(self, token: Token, message: str):
        errors.error(token, message)
        return AQAParseError(token, message)

    def _match_token(self, *token_types: str) -> bool:
        for token_type in token_types:
            if self._check(token_type):
                self._advance()
                return True
        return False

    def _consume(self, token_type: str, message: str) -> Token:
        if self._check(token_type):
            return self._advance()
        raise AQAParseError(self._peek(), message)

    def _synchronize(self) -> None:
        self._advance()

        while not self._at_end():
            if self._previous().type == NEWLINE:
                return
            self._advance()

    def _check(self, token_type: str) -> bool:
        if self._at_end():
            return False
        return self._peek().type == token_type

    def _advance(self) -> Token:
        if not self._at_end():
            self._current += 1
        return self._previous()

    def _at_end(self) -> bool:
        return self._peek().type == EOF

    def _peek(self) -> Token:
        return self.tokens[self._current]

    def _previous(self) -> Token:
        return self.tokens[self._current - 1]

    def _primary(self) -> Expr:
        if self._match_token(FALSE):
            return Literal(False)
        elif self._match_token(TRUE):
            return Literal(True)
        elif self._match_token(NONE):
            return Literal(None)
        elif self._match_token(STRING):
            return Literal(self._previous().literal)
        elif self._match_token(NUMBER):
            if self._previous().literal.isdecimal():
                return Literal(int(self._previous().literal))
            else:
                return Literal(float(self._previous().literal))
        elif self._match_token(LEFT_PAREN):
            expr = self._expression()
            self._consume(RIGHT_PAREN, "Expected ')' after expression.")
            return Grouping(expr)
        elif self._match_token(IDENTIFIER):
            return Variable(self._previous())

        raise error(self._peek(), "Expect expression")

    def _unary(self) -> Expr:
        if self._match_token(NOT, MINUS):
            return Unary(self._previous(), self._unary())

        return self._primary()

    def _factor(self) -> Expr:
        expr = self._unary()

        while self._match_token(DIVIDE, TIMES):
            expr = Binary(expr, self._previous(), self._factor())

        return expr

    def _term(self) -> Expr:
        expr = self._factor()

        while self._match_token(MINUS, ADD):
            expr = Binary(expr, self._previous(), self._factor())

        return expr

    def _comparison(self) -> Expr:
        expr = self._term()

        while self._match_token(GREATER, GREATER_EQUAL, LESS, LESS_EQUAL):
            expr = Binary(expr, self._previous(), self._term())

        return expr

    def _equality(self) -> Expr:
        expr = self._comparison()

        while self._match_token(NOT_EQUAL, EQUAL):
            expr = Binary(expr, self._previous(), self._comparison())

        return expr

    def _and(self) -> Expr:
        expr = self._equality()

        while self._match_token(AND):
            return Logical(expr, self._previous(), self._equality())

        return expr

    def _or(self) -> Expr:
        expr = self._and()

        while self._match_token(OR):
            expr = Logical(expr, self._previous(), self._and())

        return expr

    def _expression(self) -> Expr:
        return self._or()

    def _print_statement(self) -> tuple[Print]:
        return (Print(self._expression()),)

    def _while_statement(self) -> tuple[While]:
        condition = self._expression()
        statements = []

        if self._peek().type in {DO, COLON}:
            self._match_token(DO, COLON)

        while not self._match_token(END):
            if self._peek().type == EOF:
                raise error(self._peek(), "Expected END after WHILE loop")

            if (stmt := self._statement()) is not None:
                statements.extend(stmt)

        return (While(condition, statements),)

    def _for_statement(self) -> tuple[Var, While]:
        initialiser = self._var_declaration()[0]
        self._consume(TO, "Expect TO inside of FOR loop. ")
        stop = self._expression()
        statements = []

        # if start and stop are constant expressions interpreting them won't raise an undeclared variable error
        step = Literal(value=1)
        try:
            if (start_value := initialiser.initialiser.interpret()) == (
                stop_value := stop.interpret()
            ):
                condition = EQUAL
            elif start_value < stop_value:
                condition = LESS_EQUAL
            # set default step to -1 start_value > stop_value
            elif start_value > stop_value:
                condition = GREATER_EQUAL
                step = Literal(value=-1)

            if self._match_token(STEP):
                step = self._expression()
        except:
            self._consume(
                STEP,
                "step needs to be specified where start or stop are not constant expressions",
            )
            step = self._expression()
            condition = LESS_EQUAL if step.value > 0 else GREATER_EQUAL

        while not self._match_token(END):
            if self._peek().type == EOF:
                raise self._error(self._peek(), "Expected TO inside FOR loop")
            if (stmt := self._statement()) is not None:
                statements += stmt

        out = initialiser, While(
            condition=Binary(
                left=Variable(name=initialiser.name),
                operator=Token(type=condition),
                right=stop,
            ),
            body=[stmt for stmt in statements]
            + [
                Var(
                    name=initialiser.name,
                    initialiser=Binary(
                        left=Variable(name=initialiser.name),
                        operator=Token(type=ADD),
                        right=step,
                    ),
                ),
            ],
        )
        return out

    def _if_statement(self) -> tuple[If]:
        condition = self._expression()
        then_branch: list[Stmt] = []
        else_branch: list[Stmt] = []

        if self._peek().type in {THEN, COLON}:
            self._match_token(THEN, COLON)

        while not self._match_token(END):
            if self._peek().type == EOF:
                raise self._error(self._peek(), "Expected END after IF statement")

            if (stmt := self._statement()) is not None:
                then_branch.extend(stmt)

            if self._match_token(ELSE):
                while not self._match_token(END):
                    if self._peek().type == EOF:
                        raise error(self._peek(), "Expected END after IF statement")
                    stmt = self._statement()
                    if stmt is not None:
                        else_branch.extend(stmt)
                break

        return (If(condition, then_branch, else_branch),)

    def _statement_not_var(
        self,
    ) -> tuple[Print] | tuple[While] | tuple[Var, While] | tuple[If] | None:
        while True:
            if self._match_token(PRINT):
                return self._print_statement()
            elif self._match_token(WHILE):
                return self._while_statement()
            elif self._match_token(FOR):
                return self._for_statement()
            elif self._match_token(IF):
                return self._if_statement()
            elif self.tokens[self._current].type == EOF:
                return
            self._current += 1
            return

    def _var_declaration(self) -> tuple[Var]:
        name = self._consume(IDENTIFIER, "Expect variable name. ")
        initialiser = self._expression() if self._match_token(ASSIGNMENT) else None
        # consume(NEWLINE, "Expect newline after variable deceleration")
        return (Var(name, initialiser),)

    def _statement(self):
        try:
            for token in self.tokens[self._current :]:
                if token.type in {PRINT, WHILE, FOR, IF, NEWLINE}:
                    return self._statement_not_var()
                elif token.type == ASSIGNMENT:
                    return self._var_declaration()
        except AQAParseError as e:
            errors.error(e.token, e.message)
            self._synchronize()
            return None

    def parse(self):
        statements: list[Stmt] = []
        while not self._at_end():
            stmt = self._statement()
            if stmt is not None:
                statements.extend(stmt)
        return statements
