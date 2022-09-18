from pathlib import Path
import os

root_path = Path(".")

for path in root_path.glob("*.py"):
    if "exercise" in path.name:
        _, exercise_num = path.stem.split("-")
        os.system(f"cp {path.name} exercise_{exercise_num}.py")

