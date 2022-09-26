# 2022 Code Challenge - Question 18 - Counter-Controlled Repetition

## Explanation

While `for` loops are great for looping through `lists`, they can also be used
to perform *counter-controlled repetition*. In counter-controlled repetition, a block
of code repeats a pre-determined (or definite) number of times. Contrast this with how
we've used `while` loops in this challenge, which run until a user or some condition causes
the loop to end.

To write a counter-controlled loop in Python, you can use the `for` loop and the built-in
`range()` function as in this example:

```python
# `num` is a variable, so you can name it whatever you want, but this is a common name
for num in range(3):
    print(num)

```

*output*
```text
0
1
2
```

Notice that the `num` variable becomes numbers in the range 0-2. When you use `range(arg)` with
a single argument, the values of the `num` variable will be: `0...arg-1`  

If you want to have a different starting value, you can use `range()` with two arguments:

```python
for num in range(1, 4):
    print(num)

```


*output*
```text
1
2
3
```

Note that the first argument to `range()` is the starting value, and the last argument is one
more than the final printed value.

## Exercise

Using what you've learned about counter-controlled looping, create an implementation of the dice
game "Three is Free!". Here are the basic rules of the game:
- Each player (a real player and the computer) rolls a six-sided die 5 times
- If they roll a three, they get zero points added to their score
- Any other roll adds points to their score
- The first player to hit 100 points loses

Hints:
- You'll need to simulate rolling a die, so import a function that allows you to generate random numbers
- You should create two functions to make this game easier to manage:
    - `display_scoreboard(player_score, computer_score)`
        - This displays the player and computer's score in a nicely formatted output
    - `calculate_score(name)`
        - Create a variable to track the score
        - This should simulate rolling a six-sided die 5 times
        - Each roll of the die, display the amount rolled along with the `name` that rolled the score
        - If the amount rolled is not 3, add that amount to the `score` variable
        - Return the `score` variable after you've rolled the die 5 times
- In the main area of your program, you should have variables to track the player and computer score
- In a `while` loop:
    - Display the scoreboard
    - Use `input()` to prompt the user to press "Enter" to play a round (this makes the game feel more realistic)
    - Use the `calculate_score()` function to:
        - Calculate and display the player's score/die rolls
        - Calculate and display the computer's score/die rolls
    - If the player scored more than 100 points
        - Display a message saying they lost and exit the loop
    - If the computer scored more than 100 points
        - Display a message saying they lost and exit the loop


Here's an example of the program running:

```text

####################
Player Score: 0
Computer Score: 0
####################

Press `Enter` to play this round:
Player rolls 5
Player rolls 5
Player rolls 5
Player rolls 3
Player rolls 3
Computer rolls 3
Computer rolls 1
Computer rolls 5
Computer rolls 1
Computer rolls 3

####################
Player Score: 15
Computer Score: 7
####################

Press `Enter` to play this round:
Player rolls 6
Player rolls 6
Player rolls 3
Player rolls 3
Player rolls 1
Computer rolls 4
Computer rolls 3
Computer rolls 5
Computer rolls 6
Computer rolls 1

####################
Player Score: 28
Computer Score: 23
####################

Press `Enter` to play this round:
Player rolls 3
Player rolls 5
Player rolls 5
Player rolls 5
Player rolls 4
Computer rolls 3
Computer rolls 1
Computer rolls 4
Computer rolls 1
Computer rolls 6

####################
Player Score: 47
Computer Score: 35
####################

Press `Enter` to play this round:
Player rolls 1
Player rolls 1
Player rolls 1
Player rolls 1
Player rolls 4
Computer rolls 3
Computer rolls 5
Computer rolls 2
Computer rolls 1
Computer rolls 4

####################
Player Score: 55
Computer Score: 47
####################

Press `Enter` to play this round:
Player rolls 3
Player rolls 2
Player rolls 1
Player rolls 1
Player rolls 6
Computer rolls 6
Computer rolls 2
Computer rolls 4
Computer rolls 1
Computer rolls 6

####################
Player Score: 65
Computer Score: 66
####################

Press `Enter` to play this round:
Player rolls 6
Player rolls 5
Player rolls 6
Player rolls 3
Player rolls 6
Computer rolls 2
Computer rolls 3
Computer rolls 4
Computer rolls 1
Computer rolls 6

####################
Player Score: 88
Computer Score: 79
####################

Press `Enter` to play this round:
Player rolls 3
Player rolls 1
Player rolls 2
Player rolls 1
Player rolls 2
Computer rolls 4
Computer rolls 2
Computer rolls 6
Computer rolls 2
Computer rolls 2

####################
Player Score: 94
Computer Score: 95
####################

Press `Enter` to play this round:
Player rolls 6
Player rolls 1
Player rolls 5
Player rolls 5
Player rolls 4
Computer rolls 1
Computer rolls 6
Computer rolls 3
Computer rolls 3
Computer rolls 2
Player loses, computer wins!
```
