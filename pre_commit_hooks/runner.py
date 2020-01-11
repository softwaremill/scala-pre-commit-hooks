import subprocess


def run_sbt_command(task_def, missing_plugin_check_string=None, missing_plugin_error_msg=None):
    sbt_process = subprocess.run([f"sbt '{task_def}'"],
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    raw_output = sbt_process.stdout.decode("utf-8")

    if missing_plugin_check_string is not None and missing_plugin_check_string in raw_output:
        print(missing_plugin_error_msg)
    else:
        print(raw_output)

    return sbt_process.returncode
