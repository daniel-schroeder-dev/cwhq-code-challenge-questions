# 2022 Code Challenge - Question 08 

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
    # This block only runs if the score is between 6 and 10
    print("Not bad, you scored prettty high!")
else:
    # This block runs for any score 5 or less
    print("That's a pretty low score...")
```

## Exercise




## Answer
