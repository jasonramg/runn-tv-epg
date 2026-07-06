from pathlib import Path
import shutil

OUTPUT = Path("output")
DOCS_OUTPUT = Path("docs/output")


def publish():

    DOCS_OUTPUT.mkdir(parents=True, exist_ok=True)

    for file in OUTPUT.iterdir():

        if file.is_file():

            shutil.copy2(
                file,
                DOCS_OUTPUT / file.name
            )