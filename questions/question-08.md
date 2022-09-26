# 2022 Code Challenge - Question 08 - Conditional Statements

## Explanation

Have you ever wondered how a program makes a decision? For example, when you
use an app to find the closest restaurant to your current location, how does
the app *know* which restaurants to show you?

A computer program can make decisions using *Conditional Statements*. These are
statements which run a block of code whenever certain True/False conditions
are met. The `if` conditional statement comes first, and if you have additional
conditions you want to test, you can use `elif` statements. The `else` statement
is used when you want a *default* block of code to run if none of the `if` or 
`elif` conditions were `True`.

You use *Comparison Operators* to compare values and produce `True` or `False` (`bool`) results.

Some examples of different ways to use conditional statements are shown below.

### Using `if`

```python
score = 5

if score > 10:
    # This block only runs if the `score` is more than 10 
    print("You've got a high score!")
```

### Using `if` and `else`

```python
name = input("Enter your name: ")

if name == "Daniel":
    # This block only runs if the `name` is "Daniel"
    print("That's an awesome name!")
else:
    # This block runs when the `name` is anything __besides__ "Daniel"
    print("I'm unfamiliar with this name...")
```

### Using `if`, `elif`, and `else`

```python
score = 7

if score > 10:
    # This block only runs if the `score` is more than 10 
    print("Congrats, you've got a really high score!")
elif score > 5:
    # This block only runs if the score is between 6 and 10 (inclusive)
    print("Not bad, you scored prettty high!")
else:
    # This block runs for any score 5 or less
    print("That's a pretty low score...")
```

## Further Reading

If you're interested in more material about conditional statements, see these resources:
-   [CWHQ Docs - Conditional Statements](https://docs.codewizardshq.com/python/python-language/#conditional-statements)
-   [Real Python - Conditional Statements in Python](https://realpython.com/python-conditional-statements/)
-   [The Python Library Reference - Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)
-   [The Python Library Reference - Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
-   [The Python Tutorial - `if` Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
-   [Think Python - Conditionals and Recursion](https://greenteapress.com/thinkpython2/html/thinkpython2006.html)

## Exercise

Create a simple chatbot which responds to the following questions:
- What is your name?
- Who is your creator?
- What programming language are you written in?
- Tell me a joke

For any other inquiry, the chatbot should respond with something like: "I don't understand that command, sorry..."

You can display whatever response you like to each question. An example
of each possible answer the chatbot provides is shown below:


### Name response
```text
Enter command: What is your name?
My name is BoorpBazzle9000
```

### Creator response
```text
Enter command: Who is your creator?
I was created by the great DJS
```

### Programming language response
```text
Enter command: What programming language are you written in?
The greatest of all programming languages, Python!
```

### Joke response
```text
Enter command: Tell me a joke
Did you hear about the claustrophobic astronaut? He just needed a little space 😂 🤣 😂 🤣
```

### Unknown command response
```text
Enter command: What is the meaning of life?
I don't understand that command, sorry...
```

## Project Link

For a link to the running project, see [exercise_08](https://projects.pty.cwhq-apps.com/?filename=/code-challenge-2022/exercise_08/main.py)
