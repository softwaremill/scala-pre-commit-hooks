from __future__ import annotations

from colorama import Fore
from colorama import init as colorama_init

from pre_commit_hooks.runner import (
    default_argparse,
    run_git_add_modified,
    run_sbt_command,
)

TASK_SCALAFMT = "scalafmtAll"
MISSING_PLUGIN_CHECK_STRING = "Not a valid key: scalafmtAll"
MISSING_PLUGIN_ERROR_MSG = f"{Fore.RED}ERROR: scalafmt SBT plugin not present! See {Fore.BLUE}https://scalameta.org/scalafmt/docs/installation.html#sbt{Fore.RED} for installation instructions."


def main(argv=None):
    colorama_init()

    args = default_argparse("Run SBT scalafmt", argv=argv)

    sbt = run_sbt_command(
        task_def=f"{TASK_SCALAFMT}",
        missing_plugin_check_string=MISSING_PLUGIN_CHECK_STRING,
        missing_plugin_error_msg=MISSING_PLUGIN_ERROR_MSG,
        opts=args,
    )
    run_git_add_modified()

    return sbt


if __name__ == "__main__":
    exit(main())
