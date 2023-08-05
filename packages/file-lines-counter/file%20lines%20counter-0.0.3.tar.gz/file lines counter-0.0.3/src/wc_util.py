import os
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def count_lines(filepath: str):
    print("file", "|", "line count")
    print("-" * 15)
    for file in os.listdir(filepath):
        if os.path.isfile(file) and (file.endswith(".txt") or file.endswith(".csv")):
            with open(Path(filepath) / file, encoding="utf-8") as f:
                print(file, "|", len(f.readlines()))


if __name__ == "__main__":
    app()
