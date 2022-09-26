# 2022 Code Challenge - Question 11 - Indefinite Loops 

## Explanation

All of the exercises and programs we've encountered so far have run once
and then exited. Is this how all computer programs work? Have you ever
used a computer program that runs until something happens or until you
choose to exit?

To allow a program to run for an *indefinite* amount of time, programmers
use a `while` loop. The `while` loop will run until a given condition
becomes `False` or a `break` statement occurs in the loop body. Below, you'll
see a few examples of `while` loops in action.

### Counting to 5 with a `while` loop

```python
counter = 1 

while counter <= 5:  # This loop runs until the `counter` is more than 5
    print(counter)
    counter = counter + 1  # This adds `1` to the `counter` each loop
```

*output*

```text
1
2
3
4
5
```

### Prompting a user to guess a word until it's correct

```python
word = "Python"

while True:  # This loop runs until a `break` statement is encountered 
    user_guess = input("Guess a word that is a reptile and a programming language: ") 
    if user_guess == word:
        print("That's correct!")
        break  # Ends the loop
    else:
        print("Sorry, that's incorrect. Try again!")

```

*output*

```text
Guess a word that is a reptile and a programming language: Snapping Turtle
Sorry, that's incorrect. Try again!
Guess a word that is a reptile and a programming language: Crocodile 
Sorry, that's incorrect. Try again!
Guess a word that is a reptile and a programming language: Python 
That's correct!
```

## Further Reading

If you're interested in further information about `while` loops, see the following resources:
-   [CWHQ Docs - `while`](https://docs.codewizardshq.com/python/python-language/#while)
-   [Real Python - Python `while` Loops](https://realpython.com/python-while-loop/)
-   [Think Python - The `while` statement](https://greenteapress.com/thinkpython2/html/thinkpython2008.html#sec84)

## Exercise

Using a `while` loop, implement the game from the previous exercise but edit it
to run until the user guesses the correct numbers (in the correct order).

Here are the detailed instructions:

- Get a random number between 1 and 10
- Get another random number between 1 and 10
- Create a variable to hold the number of guesses (what value should it start with before the user guesses?)
- Sum the numbers and display the sum
- In a `while` loop:
    - Ask the user to guess the random numbers based on the sum
    - Increment the number of guesses the user has made
    - If the user guesses both numbers correctly (in the correct order)
        - Tell them they guessed correctly 
        - Show both of the numbers 
        - Exit the loop
    - If they guess incorrectly
        - Tell them something like: "That's incorrect, try again!"
- After the `while` loop, tell the user how many guesses it took them to get the correct answer

Here's and example run of the program:

```text
The sum of the numbers is: 6
What do you think the first number is? 3
What do you think the second number is? 2
That's incorrect, try again!
What do you think the first number is? 2
What do you think the second number is? 3
That's incorrect, try again!
What do you think the first number is? 3
What do you think the second number is? 3
That's incorrect, try again!
What do you think the first number is? 4
What do you think the second number is? 2
That's incorrect, try again!
What do you think the first number is? 2
What do you think the second number is? 4
That's incorrect, try again!
What do you think the first number is? 5
What do you think the second number is? 1
That's incorrect, try again!
What do you think the first number is? 1
What do you think the second number is? 5
That's correct!
The numbers were 1 + 5 = 6
It took you 7 guesses to get the correct answer.
```
