# 2022 Code Challenge - Question 14 - Create The Dice Game "Pig"

## Explanation

Let's take a break from learning any more major concepts and build a project with all that
you've learned so far! We'll implement a simplified version of a dice game called Pig in this project. 

Here are the rules:
- There are two players: the user and a computer opponent
- There is one six-sided die 
- Each player "rolls" the die and adds the value of the die to their number of points
    - The first player to reach 30 points wins
    - If a player rolls a 1, they lose all their points

We'll simulate rolling dice in this app, and we can pause the program and ask the user to 
press "Enter" by using an `input()` statement where we don't care about the return value, as
in this example below:

```python
# The program pauses here until the user presses Enter
input("Press enter to continue...")

print("We've continued")

# The program pauses here until the user presses Enter 
input("Press enter to continue again...")

print("Still going...")
```

## Exercise

Here are some detailed hints on how you could implement Pig in Python:
- You'll need to generate random numbers, so make sure to import the correct function from the correct module to do this.
- Create a function called `check_die(score, die_value)`
    - It should take a `score` and `die_value` as parameters
    - It will return 0 if the `die_value` is 1
    - It will return the `score` plus the `die_value` for any other situation
- Create a function called `display_scoreboard(player_score, computer_score)`
    - It should define two parameters: `player_score` and `computer_score`
    - It should display the `player_score` and `computer_score` in a nicely formatted way of your choosing
- Track the `player_score` and the `computer_score` in variables
    - These should start with an initial value before the game begins
- The main game logic should be in a `while` loop
- In this loop:
    - Prompt the user to press "Enter" to roll the die
    - Simulate "rolling" the die by generating a random number to represent a valid value of a six-sided die
    - Display the value of the die roll with a message like: "Player rolls a [die_value]"
    - Pass the `player_score` and the value of the six-sided die to `check_die()` and set the `player_score` to the return value of this function 
    - Simulate "rolling" the die again by generating another random number to represent a valid value of a six-sided die
    - Display the value of the die roll with a message like: "Computer rolls a [die_value]"
    - Pass the `computer_score` and the value of the six-sided die to `check_die()` and set the `computer_score` to the return value of this function 
    - Print the player and computer's score using the `display_scoreboard()` function
    - If the `player_score` is 30 or more:
        - Print a message telling the player they've won
        - Exit the loop
    - If the `computer_score` is 30 or more:
        - Print a message saying the computer won
        - Exit the loop

Here's an example of the program running:

```text
Press 'Enter' to roll the die...

Player rolls a 5
Computer rolls a 1

####################
Player Score: 5
Computer Score: 0
####################

Press 'Enter' to roll the die...

Player rolls a 4
Computer rolls a 3

####################
Player Score: 9
Computer Score: 3
####################

Press 'Enter' to roll the die...

Player rolls a 3
Computer rolls a 6

####################
Player Score: 12
Computer Score: 9
####################

Press 'Enter' to roll the die...

Player rolls a 3
Computer rolls a 3

####################
Player Score: 15
Computer Score: 12
####################

Press 'Enter' to roll the die...

Player rolls a 6
Computer rolls a 4

####################
Player Score: 21
Computer Score: 16
####################

Press 'Enter' to roll the die...

Player rolls a 2
Computer rolls a 6

####################
Player Score: 23
Computer Score: 22
####################

Press 'Enter' to roll the die...

Player rolls a 6
Computer rolls a 6

####################
Player Score: 29
Computer Score: 28
####################

Press 'Enter' to roll the die...

Player rolls a 5
Computer rolls a 1

####################
Player Score: 34
Computer Score: 0
####################

Player wins!
```

> Note that you could go further with this project by personalizing the app using the player's name (you'd need to prompt them for this).
> You could also ensure that if both the player and the computer score over 100 in the same round, there's a tie breaker of some sort that determines who should win (you could use whoever had the highest score)

