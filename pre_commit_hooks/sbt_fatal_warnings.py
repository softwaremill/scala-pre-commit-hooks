import argparse
from pre_commit_hooks.runner import *

ARG_ADDITIONAL_ARGS = 'add_arg'
ARG_COMPILE_SCOPE = 'scope'
DEFAULT_COMPILE_SCOPE = 'test:compile'


def main(argv=None):
    arg_p = argparse.ArgumentParser(description='Run SBT wartremover')
    arg_p.add_argument(f'--{ARG_ADDITIONAL_ARGS}', action='append',
                       help='Additional arguments for scalac, such as warning flags, can be multi-valued.')
    arg_p.add_argument(f'--{ARG_COMPILE_SCOPE}', default=DEFAULT_COMPILE_SCOPE,
                       help=f'Compile scope for the check. Default: {DEFAULT_COMPILE_SCOPE}')

    args = arg_p.parse_args(argv).__dict__

    args[ARG_ADDITIONAL_ARGS].append("-Xfatal-warnings")

    add_args = ", ".join(f'"{a}"' for a in args[ARG_ADDITIONAL_ARGS])

    return run_sbt_command(f'; clean ; set scalacOptions ++= Seq({add_args}) ; {args[ARG_COMPILE_SCOPE]}')


if __name__ == '__main__':
    exit(main())
