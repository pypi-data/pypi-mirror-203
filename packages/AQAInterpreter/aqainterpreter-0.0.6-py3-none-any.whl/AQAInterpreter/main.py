"""main program for AQAInterpreter module"""

from pprint import pprint
import click

from AQAInterpreter.scanner import Scanner
from AQAInterpreter.parser import Parser


def run(source: str, debug: bool = False) -> str:
    """evaluates `source` returning a string"""

    source += "\n"
    if debug:
        print(source)

    tokens = Scanner(source).scan_tokens()
    if debug:
        pprint(tokens)
        print()

    output: list[str] = []
    statements = Parser(tokens).parse()
    if debug:
        print(statements)

    for statement in statements:
        statement.interpret(output)

    return "".join(output)


@click.command()
@click.argument("filename", required=False)
@click.option("-c", "--cmd")
@click.option("-d", "--debug", is_flag=True, default=False, help="Show tokens and ast")
def main(filename: str, cmd: str, debug: bool):
    """source code can be read in from a file or a string
    if `debug` is True, tokens and ast are also printed"""

    if filename and cmd:
        raise click.UsageError("cannot specify both filename and command")

    if filename:
        with open(filename, encoding="utf-8") as infp:
            cmd = infp.read()
    else:
        while True:
            click.echo(run(input("> "), debug=debug).rstrip())

    click.echo(run(cmd, debug=debug).rstrip())


if __name__ == "__main__":
    main()
