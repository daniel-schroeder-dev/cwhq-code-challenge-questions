#!/usr/bin/python

from pathlib import Path

root_path = Path(".")

for path in root_path.glob("**/exercise*.py"):
    print(path)

