# 2022 Code Challenge - Question 21 

## Explanation

Congratulations on making it to the final question of this challenge! To test your knowledge
of Python and basic programming concepts, in this exercise we'll implement a card game called
"Matchmaker". There are a few techniques you can use (which we haven't learned throughout this challenge)
to implement this game. All of them revolve around manipulating lists in some way, as you'll create 
a list of `dict` representing a deck of cards in this challenge.

To get a random item from a list, you can use the `choice()` function from the `random` module:

```python
from random import choice

names = ["Daniel", "Django", "Jim"]
random_name = choice(names)

print(random_name)  # Django
```

To build a deck of cards, you can use nested loops. The general pattern would be:

```python
suits = ["diamonds", "hearts", "spades", "clubs"]
deck = []

for suit in suits:
    for rank in range(1, 11):
        # build a `card` `dict` with the suit and rank
        # append it to the `deck`
```

To shuffle a `list`, you can use the `shuffle` function from the `random` module:

```python
from random import shuffle

names = ["Daniel", "Django", "Jim"]
shuffle(names)

print(names)  # ["Django", "Daniel", "Jim"]
```

To remove an item from a `list` (not using an index) you can use the `list.remove()` method:

```python
names = ["Daniel", "Django", "Jim"]

names.remove("Django")
print(names)  # ["Daniel", "Jim"]
```

To get the index of an item in a `list`, you can use the `list.index()` method:

```python
names = ["Daniel", "Django", "Jim"]

django_index = names.index("Django")
print(django_index)  # 1
```

To get the index of an item while looping through a `list`, use the `enumerate()` function:

```python
names = ["Daniel", "Django", "Jim"]

for index, name in enumerate(names):
    print(index, name)

```

*output*
```text
0 Daniel
1 Django
2 Jim
```


## Exercise

The rules of "Matchmaker" are simple. Using a shuffled deck, each player gets to pick two cards
each round. If the cards are a match, the player keeps the cards and they are removed from the deck.
Once the deck is empty, the game ends. The player with the most cards wins. You'll have one human
player and one computer player in your implementation of this game.

Hints:
- Import the `shuffle` and `choice` functions from the `random` module
- Define a function called `create_deck()` which:
    - Creates a `list` of `suits` representing the four suits in a standard deck of cards:
        - diamonds, hearts, clubs, spades
    - Creates an empty `deck` `list`
    - Loops through the `list` of `suits`
        - Loops through the numbers 1 thru 10. These are the ranks (this is nested inside the `suits` loop)
            - Builds a `card` `dict` from the suit and rank
            - Appends the `card` `dict` to the `deck`
    - The function should return the `deck` after it's built
- Make a helper function called `display_deck(deck)`
    - This should loop through all cards in the `deck` and display them along with their index number
    - You'll only use this for developing/testing your game, you shouldn't display this information
    when someone is actually playing the game
- Make a function called `display_cards(player_name, cards)`
    - This function should display the player's name and loop and display all of the `cards` in a nicely formatted way

- In the main application area:
    - Create a `deck` using the `create_deck()` function
    - Shuffle the deck
    - Create a `player_cards` empty `list`
    - Create a `computer_cards` empty `list`

- In a `while loop:
    - Display the deck using `display_deck()`
        - Only do this while developing/testing the game
    - Display each players cards using `display_cards()`
    - Display the number of cards left in the `deck`
    - To get the player's cards:
        - Prompt the user for the index number of the first card they want to choose
        - Pull this card from the `deck`
        - Display this card along with the index number
        - Repeat the above steps for the second card the player chooses
    - Once you have both cards that the player chose, see if the ranks match and ensure they aren't the same card
        - If the above is true:
            - Display: "That's a match!"
            - Append each card to the `player_cards` list
            - Remove each card from the `deck` (don't do this by index number, use a method shown in the Explanation)
    - Check if the deck is empty, and exit the loop if so
    - To get the computer's cards
        - Get two random cards from the deck
        - Get the index of each card
    - Once you have both cards that the computer chose, see if the ranks match and ensure they aren't the same card
        - If the above is true:
            - Display: "That's a match!"
            - Append each card to the `computer_cards` list
            - Remove each card from the `deck` (don't do this by index number, use a method shown in the Explanation)
    - Check if the deck is empty, and exit the loop if so

- After the `while` loop:
    - Display a message like: "Final cards for each player"
    - Display the cards of each player
    - If the player has more cards than the computer
        - Display a message like: "Player wins!"
    - If the computer has more cards than the player 
        - Display a message like: "Computer wins!"
    - Otherwise, it's a tie and display: "It's a tie!"

Example output:

```text

####################
Player's cards:
####################


####################
Computer's cards:
####################

There are 8 cards left in the deck
Choose first card (by index): 0
Player chooses {'suit': 'diamonds', 'rank': 1} at index 0
Choose second card (by index): 1
Player chooses {'suit': 'hearts', 'rank': 4} at index 1
Computer chooses {'suit': 'hearts', 'rank': 2} at index 5
Computer chooses {'suit': 'hearts', 'rank': 4} at index 1

####################
Player's cards:
####################


####################
Computer's cards:
####################

There are 8 cards left in the deck
Choose first card (by index): 0
Player chooses {'suit': 'diamonds', 'rank': 1} at index 0
Choose second card (by index): 2
Player chooses {'suit': 'diamonds', 'rank': 4} at index 2
Computer chooses {'suit': 'hearts', 'rank': 1} at index 4
Computer chooses {'suit': 'diamonds', 'rank': 4} at index 2

####################
Player's cards:
####################


####################
Computer's cards:
####################

There are 8 cards left in the deck
Choose first card (by index): 1
Player chooses {'suit': 'hearts', 'rank': 4} at index 1
Choose second card (by index): 2
Player chooses {'suit': 'diamonds', 'rank': 4} at index 2
That's a match!
Computer chooses {'suit': 'hearts', 'rank': 3} at index 5
Computer chooses {'suit': 'hearts', 'rank': 1} at index 2

####################
Player's cards:
{'suit': 'hearts', 'rank': 4}
{'suit': 'diamonds', 'rank': 4}
####################


####################
Computer's cards:
####################

There are 6 cards left in the deck
Choose first card (by index): 0
Player chooses {'suit': 'diamonds', 'rank': 1} at index 0
Choose second card (by index): 2
Player chooses {'suit': 'hearts', 'rank': 1} at index 2
That's a match!
Computer chooses {'suit': 'hearts', 'rank': 3} at index 3
Computer chooses {'suit': 'hearts', 'rank': 2} at index 1

####################
Player's cards:
{'suit': 'hearts', 'rank': 4}
{'suit': 'diamonds', 'rank': 4}
{'suit': 'diamonds', 'rank': 1}
{'suit': 'hearts', 'rank': 1}
####################


####################
Computer's cards:
####################

There are 4 cards left in the deck
Choose first card (by index): 0
Player chooses {'suit': 'diamonds', 'rank': 3} at index 0
Choose second card (by index): 3
Player chooses {'suit': 'hearts', 'rank': 3} at index 3
That's a match!
Computer chooses {'suit': 'hearts', 'rank': 2} at index 0
Computer chooses {'suit': 'diamonds', 'rank': 2} at index 1
That's a match!
Final cards for each player

####################
Player's cards:
{'suit': 'hearts', 'rank': 4}
{'suit': 'diamonds', 'rank': 4}
{'suit': 'diamonds', 'rank': 1}
{'suit': 'hearts', 'rank': 1}
{'suit': 'diamonds', 'rank': 3}
{'suit': 'hearts', 'rank': 3}
####################


####################
Computer's cards:
{'suit': 'hearts', 'rank': 2}
{'suit': 'diamonds', 'rank': 2}
####################

Player wins!
```
