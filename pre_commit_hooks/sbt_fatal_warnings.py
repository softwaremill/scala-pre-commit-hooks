import argparse
from pre_commit_hooks.runner import *

ARG_ADDITIONAL_ARGS = 'add_args'
ARG_COMPILE_SCOPE = 'scope'
DEFAULT_COMPILE_SCOPE = 'test:compile'


def main(argv=None):
    arg_p = argparse.ArgumentParser(description='Run SBT wartremover')
    arg_p.add_argument('--{}'.format(ARG_ADDITIONAL_ARGS), default=None,
                       help='Additional arguments for scalac, such as warning flags, comma-separated.')
    arg_p.add_argument('--{}'.format(ARG_COMPILE_SCOPE), default=DEFAULT_COMPILE_SCOPE,
                       help='Compile scope for the check. Default: {}'.format(DEFAULT_COMPILE_SCOPE))

    args = arg_p.parse_args(argv).__dict__

    add_args = args[ARG_ADDITIONAL_ARGS]+"," if args[ARG_ADDITIONAL_ARGS] is not None else ''

    return run_sbt_command('; clean ; set scalacOptions ++= Seq({}"-Xfatal-warnings") ; {}'.format(
        add_args, args[ARG_COMPILE_SCOPE]))


if __name__ == '__main__':
    exit(main())
