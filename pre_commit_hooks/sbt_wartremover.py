import argparse
from pre_commit_hooks.runner import *
from colorama import init as colorama_init, Fore

ARG_WARTREMOVER_ARGS = 'warts'
ARG_COMPILE_SCOPE = 'scope'
DEFAULT_WARTREMOVER_ARGS = 'Warts.unsafe'
DEFAULT_COMPILE_SCOPE = 'test:compile'
MISSING_PLUGIN_CHECK_STRING = 'error: not found: value wartremoverErrors'
MISSING_PLUGIN_ERROR_MSG = f'{Fore.RED}ERROR: wartremover SBT plugin not present! See {Fore.BLUE}https://www.wartremover.org/doc/install-setup.html{Fore.RED} for installation instructions.'


def main(argv=None):
    colorama_init()

    arg_p = argparse.ArgumentParser(description='Run SBT wartremover')
    arg_p.add_argument(f'--{ARG_WARTREMOVER_ARGS}', default=DEFAULT_WARTREMOVER_ARGS,
                       help=f'Value for wartremoverErrors, as per https://www.wartremover.org/doc/install-setup.html . Default: {DEFAULT_WARTREMOVER_ARGS}')
    arg_p.add_argument(f'--{ARG_COMPILE_SCOPE}', default=DEFAULT_COMPILE_SCOPE,
                       help=f'Compile scope for the wartremover check. Default: {DEFAULT_COMPILE_SCOPE}')
    arg_p.print_help()

    args = arg_p.parse_args(argv).__dict__

    return run_sbt_command(f'; clean ; set wartremoverErrors ++= {args[ARG_WARTREMOVER_ARGS]}; {args[ARG_COMPILE_SCOPE]}', MISSING_PLUGIN_CHECK_STRING, MISSING_PLUGIN_ERROR_MSG)


if __name__ == '__main__':
    exit(main())
