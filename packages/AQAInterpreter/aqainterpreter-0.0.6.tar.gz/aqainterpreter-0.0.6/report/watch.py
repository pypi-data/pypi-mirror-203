from inotify.adapters import Inotify
import inotify.adapters
import subprocess
import os


def handle_event(event_handler: Inotify, dir: str, cmd: str) -> None:
    event_handler.add_watch(dir)
    for event in event_handler.event_gen(yield_nones=False):
        _, type_names, path, filename = event
        if filename in os.listdir(path) and type_names == ["IN_MODIFY"]:
            print(f"{path=}, {filename=}, {type_names=}")
            subprocess.call(cmd, shell=True)
            return


def compile_on(dir: str, cmd: str) -> None:
    while True:
        event_handler = inotify.adapters.Inotify()
        handle_event(event_handler, dir, cmd)


def main() -> None:
    # compile_on("report", "./report/compile_report.sh")
    compile_on("report", "./report/compile_report_no_font.sh")


if __name__ == "__main__":
    main()


""" 
rm -r AQAInterpreter/__pycache__
tree ./AQAInterpreter   # add this to source code inside of ``` ```
for every file in aqainterpreter add file name followed by ```python ...CONTENT```



 """
