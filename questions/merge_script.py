#!/usr/bin/python

from pathlib import Path
from os import system

code_challenge_path = Path("/home/daniel/Public/cwhq/curriculum/projects/code-challenge-2022")
root_path = Path(".")


for path in list(root_path.glob("**/exercise*.py")):
    folder_path = code_challenge_path / path.stem
    folder_path.mkdir()
    system(f"cp {path} {folder_path}/main.py")
