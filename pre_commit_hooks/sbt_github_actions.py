from pre_commit_hooks.runner import run_sbt_command
from colorama import init as colorama_init, Fore

SBT_TASK = 'githubWorkflowGenerate'
MISSING_PLUGIN_CHECK_STRING = f'Not a valid key: {SBT_TASK}'
MISSING_PLUGIN_ERROR_MSG = f'{Fore.RED}ERROR: sbt-github-actions SBT plugin not present! See {Fore.BLUE}https://github.com/djspiewak/sbt-github-actions#sbt-github-actions{Fore.RED} for installation instructions.'


def main(argv=None):
    colorama_init()
    return run_sbt_command(f'; clean ; {SBT_TASK}', MISSING_PLUGIN_CHECK_STRING, MISSING_PLUGIN_ERROR_MSG)


if __name__ == '__main__':
    exit(main())
