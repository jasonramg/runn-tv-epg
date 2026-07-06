import subprocess


def git(*args):

    subprocess.run(
        ["git", *args],
        check=True
    )