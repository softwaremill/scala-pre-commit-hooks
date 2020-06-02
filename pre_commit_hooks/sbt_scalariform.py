from pre_commit_hooks.runner import run_sbt_command
from colorama import init as colorama_init, Fore

TASK_SCALARIFORM = 'scalariform'
MISSING_PLUGIN_CHECK_STRING = 'Not a valid key: scalariform'
MISSING_PLUGIN_ERROR_MSG = f'{Fore.RED}ERROR: scalariform SBT plugin not present! See {Fore.BLUE}https://github.com/sbt/sbt-scalariform{Fore.RED} for installation instructions.'

def main(argv=None):
    colorama_init()

    return run_sbt_command(TASK_SCALARIFORM, MISSING_PLUGIN_CHECK_STRING, MISSING_PLUGIN_ERROR_MSG)


if __name__ == '__main__':
    exit(main())
