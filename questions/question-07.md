# 2022 Code Challenge - Question 07 - User Input

## Explanation

So far, all of the exercises/programs we've written have used data provided
by the programmer. When you use a program in the real-world, the program often
asks you for some data before it performs a task. 

In Python, the `input()` function allows us to ask a user for some data. It always
returns a `str` data type:

```python
username = input("Enter your username: ")

print(f"Welcome, {username}!")
```

If you are expecting a numeric data type (`int` or `float`) from the user, then you
need to convert the return value of `input()` to the appropriate type. The easiest
way is to wrap the conversion function around the `input()` function, as in the examples
below:

```python
number1 = int(input("Enter an integer: "))
number2 = float(input("Enter a decimal number: "))

total = number1 + number2
print(f"{number1} + {number2} = {total}")
```

## Exercise

You've been hired to create an app that let's users know how to evenly divide a pizza
between friends. Your app should do the following:
- Prompt the user for their name
- Prompt the user for the number of friends they'll split the pizza with
- Calculate the number of slices each friend gets from the pizza (assume there are 8 slices in every pizza)
- Display the number of slices each friend gets from the pizza

An example of a possible program is shown below:


```text
What is your name? Daniel
How many friends will you be splitting the pizza with? 3
Each person gets 2.6666666666666665 slices of pizza.
```

Note that some decimal numbers (as in the one above) will have a repeating decimal portion, so the output
may look a bit weird depending on the number of friends you are splitting a pizza with.
