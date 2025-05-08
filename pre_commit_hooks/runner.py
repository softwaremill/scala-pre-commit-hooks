import subprocess


def run_sbt_command(
    task_def: str,
    missing_plugin_check_string: str | None = None,
    missing_plugin_error_msg: str | None = None,
):
    sbt_process = subprocess.run(
        [f"sbt '{task_def}'"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
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
