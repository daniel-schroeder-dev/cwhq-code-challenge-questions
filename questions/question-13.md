# 2022 Code Challenge - Question 13 - Function Parameters and Return Values

## Explanation

Now that you know how to create your own functions, let's learn how to send data 
into and out of a function! 

You may have noticed that the `print()` function takes
data into the `()` and then does something (displays it to the screen) with that data.
The *something* that goes into the `()` is called a function parameter.

Here's how you define a function parameter (or an argument, depending on how it's used, which you'll see later):

```python
# `num1` and `num2` are the parameters of the `add()` function
def add(num1, num2):
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

```

The parameter represents an unknown value when the function is defined. The parameter is
given a value whenever the function is called and the function caller passes values into
the `()`. When you pass values into `()`, they become known as arguments.

The example below shows how function arguments give values to function parameters:

```python
def add(num1, num2):
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")


# 2 (num1) and 3 (num2) are the arguments of the `add()` function
add(2, 3)  # 2 + 3 = 5

# 3 (num1) and 4 (num2) are the arguments of the `add()` function
add(3, 4)  # 3 + 4 = 7
```

Sending data into a function is great and all, but have you noticed that functions like
`input()` and `randint()` return data after they are called? You can send data out of a
function using a `return` statement:

```python
def add(num1, num2):
    total = num1 + num2
    return total  # This is sent out of the function when the function is called


total = add(2, 3)
print(total)  # 5

total = add(3, 4)
print(total)  # 7
```

## Further Reading

If you're interested in more information about functions in Python, see the following resources:
-   [CWHQ Docs - User-defined functions](https://docs.codewizardshq.com/python/python-language/#user-defined-functions)
-   [Real Python - Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
-   [The Python Tutorial - Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
-   [Think Python - Functions](https://greenteapress.com/thinkpython2/html/thinkpython2004.html)
-   [Think Python - Fruitful Functions](https://greenteapress.com/thinkpython2/html/thinkpython2007.html)

## Exercise

Using what you've learned about function parameters/arguments and returning values from
a function, create a program that tells users what year someone was born based on their
current age. The year may be off by 1 or so since we're not taking into account their
birth month.

Here are some hints for a possible implementation of this program:
- Create a function called `calculate_birth_year(age)`
    - Define one parameter, `age`
    - Calculate the birth year based on that `age`
    - Return the `birth_year` from the function
- Prompt the user for an age (in years)
- Calculate the birth year (roughly) of that age using your `calculate_birth_year()` function
- Display the birth year

Here's an example run of the program:

```text
How old are you (in years)? 36
You were born in (roughly) 1986.
```
