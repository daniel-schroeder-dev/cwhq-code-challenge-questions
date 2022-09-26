# 2022 Code Challenge - Question 10 - Built-In Modules

## Explanation

Python is often called a *batteries-included* language because it comes with
so much functionality baked-in to the language. Besides `print()` and `input()`,
there are tons of built-in functions that you can use in Python which you can
see here [Built-in Functions](https://docs.python.org/3/library/functions.html).

In addition to built-in functions, Python also has hundreds of built-in *modules*, which are
collections of functions and other utilities for performing common programming tasks. You 
can see a list of all of the built-in Python modules here [The Python Standard Library](https://docs.python.org/3/library/index.html).

We'll use the `random` module a few times in the remainder of this challenge. The first
function we'll use from the module is the `randint()` function, and we can gain access
to it and use it like this:

```python
# You must `import` functions from modules
from random import randint

random_number = randint(1, 10)  # Generates a random number between 1 and 10
```

## Further Reading

If you're interested in more information on Python's built-in modules, see these resources:
- [CWHQ Docs - Built-in Modules](https://docs.codewizardshq.com/python/python-language/#built-in-modules)
- [Real Python - Python Modules and Packages - An Introduction](https://realpython.com/python-modules-packages/)

## Exercise

Using the `randint()` function from the `random` module, implement the following
game:
- Get a random number between 1 and 10
- Get another random number between 1 and 10
- Sum the numbers and display the sum
- Ask the user to guess the random numbers based on the sum
- If the user guesses both numbers correctly (in the correct order), tell them they win $100
- If they guess incorrectly, tell them something like: "Better luck next time"
- Show both of the numbers at the end of the game

Here are a few examples of running the program with different
results:

### Neither number correct

```text
The sum of the numbers is: 8
What do you think the first number is? 4
What do you think the second number is? 4
Sorry, better luck next time!
The numbers were 2 + 6 = 8
```

### Both numbers correct

```text
The sum of the numbers is: 11
What do you think the first number is? 8
What do you think the second number is? 3
That's correct! You win $100.
The numbers were 8 + 3 = 11
```

## Project Link

For a link to the running project, see: [exercise_10](https://projects.pty.cwhq-apps.com/?filename=/code-challenge-2022/exercise_10/main.py)
