import argparse
import subprocess
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Opts:
    project_dir: str | None = None
    clean: bool = True
    varargs: dict = field(default_factory=dict)


def default_argparse(
    description: str,
    argv=None,
    additional_args: list[Callable[[argparse.ArgumentParser], None]] = [],
) -> Opts:
    arg_p = argparse.ArgumentParser(description=description)
    arg_p.add_argument(
        "--project-dir",
        default=None,
        help="Path to build.sbt. Default: Project root",
    )
    arg_p.add_argument(
        "--no-clean",
        action="store_true",
        default=False,
        help="Turn off sbt clean. Default: False",
    )
    for fn in additional_args:
        fn(arg_p)
    varags = vars(arg_p.parse_args(argv))
    return Opts(
        project_dir=varags.pop("project_dir", None),
        clean=not varags.pop("no_clean", False),
        varargs=varags,
    )


def run_sbt_command(
    task_def: str,
    missing_plugin_check_string: str | None = None,
    missing_plugin_error_msg: str | None = None,
    opts: Opts = Opts(),
):
    print(f"Running SBT command: {task_def} with options: {opts}")
    if opts.clean:
        task_def = f"; clean ; {task_def}"
    else:
        task_def = f"; {task_def}"
    sbt_process = subprocess.run(
        [f"sbt '{task_def}'"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        cwd=opts.project_dir,
    )
    raw_output = sbt_process.stdout.decode("utf-8")

    if (
        missing_plugin_check_string is not None
        and missing_plugin_check_string in raw_output
    ):
        print(missing_plugin_error_msg)
    else:
        print(raw_output)

    return sbt_process.returncode


def run_git_add_modified():
    """Adds stages files if changes are detected."""
    try:
        # Check if there are modified files before running git add -u
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
        )

        if status.stdout.strip():  # If there are modified files
            print("Staged formatted files.")
            return subprocess.run(["git", "add", "-u"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return e.returncode
