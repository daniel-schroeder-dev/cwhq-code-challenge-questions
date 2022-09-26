# 2022 Code Challenge - Question 12 - User-Defined Functions

## Explanation

You've seen some built-in Python functions and some functions included in 
Python modules, but did you know you could build your own functions? Functions
are a handy tool for grouping related pieces of code together under a common
name. They are kind of like a variable in that you get to name them, but instead
of holding a piece of data, they hold statements that you can execute by using
the function name followed by `()` characters.

Consider this program, which generates a random arithmetic expression:

```python
from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)

random_number = randint(1, 4)

operator = ""

if random_number == 1:
    operator = "+"
elif random_number == 2:
    operator = "-"
elif random_number == 3:
    operator = "/"
elif random_number == 4:
    operator = "*"

expression = f"{num1} {operator} {num2}"

print(expression)
```

It's not clear at a glance what that program does, right? You have to read
each line of code and then try to understand what the overall goal of the 
program is. Also, if you wanted to generate multiple random expressions, you'd
have to copy/paste all of that code again, yuck!

This is where function definitions come in really handy! We can create a function
called `generate_arithmetic_expression()` and put most of the code from
the above example inside the function definition. Then, whenever we *call* the function
(by typing the function name followed by `()` characters) all of the code inside the
function will run.

Here's an example of what the program could look like if we wanted to generate three
random arithmetic expressions:

```python
# Imports usually are __outside__ of any function definition
from random import randint


# This doesn't __do__ anything but give a name to all of the code inside of it
def generate_arithmetic_expression():
    num1 = randint(1, 10)
    num2 = randint(1, 10)

    random_number = randint(1, 4)

    operator = ""

    if random_number == 1:
        operator = "+"
    elif random_number == 2:
        operator = "-"
    elif random_number == 3:
        operator = "/"
    elif random_number == 4:
        operator = "*"

    expression = f"{num1} {operator} {num2}"

    print(expression)


# We have to __call__ the function to run the code inside of it
generate_arithmetic_expression()  # 3 + 2
generate_arithmetic_expression()  # 5 / 1
generate_arithmetic_expression()  # 4 - 7
```

## Further Reading

If you're interested in more information about user-defined functions, see these resources:
-   [CWHQ Docs - User-defined functions](https://docs.codewizardshq.com/python/python-language/#user-defined-functions)
-   [Real Python - Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
-   [The Python Tutorial - Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
-   [Think Python - Functions](https://greenteapress.com/thinkpython2/html/thinkpython2004.html)
-   [Think Python - Fruitful Functions](https://greenteapress.com/thinkpython2/html/thinkpython2007.html)

## Exercise

Using what you've learned about function definitions, move all of you Chatbot
code from exercise 8 into a function called `run_chatbot()`. Then, create
the following program using this function:

- Define the `run_chatbot()` function with all of the code from exercise 8 inside it
- In a `while` loop:
    - Prompt the user to pick one of the following options (they should type 1 or 2 here):
        1. Run the chatbot
        2. Exit the program
    - If the user chooses to run the chatbot:
        - Call the `run_chatbot()` function
    - If the user chooses to exit the program:
        - Say "Goodbye!"
        - Exit the loop

Here's an example of the program running:

```text
Do you want to (1) run the chatbot or (2) exit the program? 1
Enter command: What is your name?
My name is BoorpBazzle9000
Do you want to (1) run the chatbot or (2) exit the program? 1
Enter command: Tell me a joke
Did you hear about the claustrophobic astronaut? He just needed a little space 😂 🤣 😂 🤣
Do you want to (1) run the chatbot or (2) exit the program? 2
Goodbye!
```
