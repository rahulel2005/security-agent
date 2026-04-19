import os
import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }


def run_validation():
    checks = []

    if os.path.exists("requirements.txt"):
        pass

    checks.append(("semgrep", run_command("semgrep --config=auto --json > findings_after.json")))

    return checks


def validation_passed(checks):
    return all(item[1]["returncode"] == 0 for item in checks)