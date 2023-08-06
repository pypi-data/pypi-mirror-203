"""adds tree and code for technical solution in `report.md` from disk"""

from pathlib import Path
import subprocess
import sys

lst = (
    (".gitignore", "text"),
    ("LICENSE", "text"),
    ("pyproject.toml", "toml"),
    ("AQAInterpreter/__init__.py", "python"),
    ("AQAInterpreter/main.py", "python"),
    ("AQAInterpreter/errors.py", "python"),
    ("AQAInterpreter/tokens.py", "python"),
    ("AQAInterpreter/scanner.py", "python"),
    ("AQAInterpreter/environment.py", "python"),
    ("AQAInterpreter/parser.py", "python"),
    ("AQAInterpreter/interpreter.py", "python"),
    ("AQAInterpreter/test_.py", "python"),
)


out = (
    "```\n"
    + subprocess.run(
        f"tree --prune -P '{'|'.join(Path(row[0]).name for row in lst)}'",
        shell=True,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.rstrip()
    + "\n```"
)


TEMPLATE = """
## {}
``` {{.{} .numberLines}}
{}
```
"""


for file, file_ext in lst:
    out += TEMPLATE.format(file, file_ext, open(file, encoding="utf-8").read())


with open(sys.argv[1], encoding="utf-8") as infp:
    content = infp.read()

content = content.replace("\\TECHNICAL_SOLUTION", out)

with open(sys.argv[1], "w", encoding="utf-8") as outfile:
    outfile.write(content)
