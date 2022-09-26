# 2022 Code Challenge - Question 06  - Arithmetic Tables

## Explanation

Now that you've worked with data types, printing, variables, `f-strings`, and
the basic arithmetic operators, you're ready to build a simple project! Before 
outlining the project goals, here are a few extra techniques around printing 
`str` data that you can use to make your project stand out:

```python
# You can multiply `str` data to create copies of the data
threes = "3" * 5
print(threes)  # 33333

# You can pass multiple arguments to `print()`
print("Hello", "world")  # Hello world

# Combining `str` multiplication with `print()`
print("username", "-" * 3, "password")  # username --- password

# The `\n` character add an additional newline to a `print()` statement
print("\n")  # This will have 2 blank lines before the next `print()` statement
```

## Exercise

To practice what you've learned so far, try to create 4 arithmetic tables
which use 10 as the `root` number. You should perform the 4 arithmetic
operations on the `root` number with the numbers 1 through 5 and display
the results in a table format. Use variables, all of the arithmetic operators,
`f-strings`, and the `print()` function to complete this project. 

Here's an example of how the output could look:


```text
   Addition Table
    ------------
    10 + 1 = 11
    10 + 2 = 12
    10 + 3 = 13
    10 + 4 = 14
    10 + 5 = 15
    ------------


  Subtraction Table
    ------------
    10 - 1 = 9
    10 - 2 = 8
    10 - 3 = 7
    10 - 4 = 6
    10 - 5 = 5
    ------------


  Multiplication Table
    ------------
    10 * 1 = 10
    10 * 2 = 20
    10 * 3 = 30
    10 * 4 = 40
    10 * 5 = 50
    ------------


   Division Table
    ------------
    10 / 1 = 10.0
    10 / 2 = 5.0
    10 / 3 = 3.3333333333333335
    10 / 4 = 2.5
    10 / 5 = 2.0
    ------------
```
