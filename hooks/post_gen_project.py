import subprocess
from typing import List


def run_with_message(command: List[str]) -> int:
    print("»", " ".join(command))
    result = subprocess.run(command)
    if result.returncode != 0:
        exit(result.returncode)


def git_init() -> None:
    commands = (
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial commit"]
    )

    for command in commands:
        code = run_with_message(command)


def compile_requirements() -> None:
    run_with_message(["make", "requirements"])


compile_requirements()

if '{{ cookiecutter.init_git }}'.lower() == 'y':
    git_init()
