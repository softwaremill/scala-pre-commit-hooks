from __future__ import annotations

import argparse

from pre_commit_hooks.runner import default_argparse, run_sbt_command

ARG_ADDITIONAL_ARGS = "add_arg"
ARG_COMPILE_SCOPE = "scope"
DEFAULT_COMPILE_SCOPE = "test:compile"


def main(argv=None):
    def arg_append(arg_p: argparse.ArgumentParser) -> None:
        arg_p.add_argument(
            f"--{ARG_ADDITIONAL_ARGS}",
            action="append",
            help="Additional arguments for scalac, such as warning flags, can be multi-valued.",
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
        additional_args=[arg_append, arg_compile_scope],
    )
    addtl_args = args.varargs.get(ARG_ADDITIONAL_ARGS, [])
    if not addtl_args:
        addtl_args = []
    if "-Xfatal-warnings" not in addtl_args:
        addtl_args.append("-Xfatal-warnings")

    add_args = ", ".join(f'"{a}"' for a in addtl_args)

    return run_sbt_command(
        task_def=f"set scalacOptions ++= Seq({add_args})",
        opts=args,
    )


if __name__ == "__main__":
    exit(main())
