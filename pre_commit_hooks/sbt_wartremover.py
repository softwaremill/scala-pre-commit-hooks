from __future__ import annotations

import argparse

from colorama import Fore
from colorama import init as colorama_init

from pre_commit_hooks.runner import default_argparse, run_sbt_command

ARG_WARTREMOVER_ARGS = "warts"
ARG_COMPILE_SCOPE = "scope"
DEFAULT_WARTREMOVER_ARGS = "Warts.unsafe"
DEFAULT_COMPILE_SCOPE = "test:compile"
MISSING_PLUGIN_CHECK_STRING = "error: not found: value wartremoverErrors"
MISSING_PLUGIN_ERROR_MSG = f"{Fore.RED}ERROR: wartremover SBT plugin not present! See {Fore.BLUE}https://www.wartremover.org/doc/install-setup.html{Fore.RED} for installation instructions."


def main(argv=None):
    colorama_init()

    def arg_wartremover(arg_p: argparse.ArgumentParser) -> None:
        arg_p.add_argument(
            f"--{ARG_WARTREMOVER_ARGS}",
            default=DEFAULT_WARTREMOVER_ARGS,
            help=f"Value for wartremoverErrors, as per https://www.wartremover.org/doc/install-setup.html . Default: {DEFAULT_WARTREMOVER_ARGS}",
        )

    def arg_compile_scope(arg_p: argparse.ArgumentParser) -> None:
        arg_p.add_argument(
            f"--{ARG_COMPILE_SCOPE}",
            default=DEFAULT_COMPILE_SCOPE,
            help=f"Compile scope for the check. Default: {DEFAULT_COMPILE_SCOPE}",
        )

    args = default_argparse(
        description="Run SBT wartremover",
        argv=argv,
        additional_args=[arg_wartremover, arg_compile_scope],
    )

    return run_sbt_command(
        task_def=f"set wartremoverErrors ++= {args.varargs.get(ARG_WARTREMOVER_ARGS)}; {args.varargs.get(ARG_COMPILE_SCOPE)}",
        missing_plugin_check_string=MISSING_PLUGIN_CHECK_STRING,
        missing_plugin_error_msg=MISSING_PLUGIN_ERROR_MSG,
        opts=args,
    )


if __name__ == "__main__":
    exit(main())
