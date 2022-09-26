#!/usr/bin/python

for num in range(11, 22):
    text = f"""
## Project Link

For a link to the running project, see: [exercise_{num}](https://projects.pty.cwhq-apps.com/?filename=/code-challenge-2022/exercise_{num}/main.py)
    """
    with open(f"question-{num}.md", mode="at", encoding="utf-8") as file:
        file.write(text)
