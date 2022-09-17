# 2022 Code Challenge - Question 19 

## Explanation

We're in the final leg of this challenge, congrats for making it this far! To finish this challenge,
we'll look at one more data structure in Python, the dictionary (`dict`). 

A `dict` holds a collection of items, like a `list`, but unlike a `list`, a `dict` organizes items
in key/value pairs, not by index number. This comes in handy when you want to store some information
about a single entity (like a user, enemy, spaceship, etc.) but you want to be able to access the information
by name and not index number.

Consider a typical CWHQ student or staff member. Somewhere in the CWHQ codebase, we're tracking different data
points about each user using a data structure like Python's `dict`. Here are some hypothetical user `dict`s:

```python
user1 = {
    "username": "danielj",
    "role": "Curriculum Developer",
    "is_active": True,
    "year_joined": 2020,
}

user2 = {
    "username": "charlieg",
    "role": "Forum Moderator",
    "is_active": False,
    "year_joined": 2017,
}
```

Notice that each key/value pair is separated by a `:`, and each `dict` holds data about a single entity (users in this case).

To access data in a `dict`, you use the same `[]` characters as a `list`, but you use the key to get the value, not
an index number:

```python
user1 = {
    "username": "danielj",
    "role": "Curriculum Developer",
    "is_active": True,
    "year_joined": 2020,
}

user2 = {
    "username": "charlieg",
    "role": "Forum Moderator",
    "is_active": False,
    "year_joined": 2017,
}

user1_username = user1["username"]
print(f"User 1's username is {user1_username}")  # User 1's username is daniel

user2_role = user2["role"]
print(f"User 2's role is {user2_role}")  # User 2's role is Forum Moderator
```

To add or update data in a `dict`, you set the data at a key (which may or may not exist) to a value:

```python
user1 = {
    "username": "danielj",
    "role": "Curriculum Developer",
    "is_active": True,
    "year_joined": 2020,
}

user1["username"] = "djs"  # This updates the `user1` dict
user1["favorite_food"] = "burritos"  # This adds data to the `user1` dict

print(user1)
```

*output*
```text
{
    'username': 'djs', 
    'role': 'Curriculum Developer', 
    'is_active': True, 
    'year_joined': 2020, 
    'favorite_food': 'burritos'
}
```


## Exercise

Now that you've seen how to use the `dict` data structure, create a program that simulates a fight
between a player and computer opponent. 

Hints:
- You'll use random numbers for a few things in this program, so make sure to import the appropriate function from the appropriate module
- Create two `dict`s, one representing a player and the other representing the computer. They should have the following key/value pairs:
    - `username` -> Prompt the user for their username. The computer's username can be whatever you want.
    - `health` -> Generate a random number between 50 and 100 for the player and computer's health.
    - `attack_strength` -> Generate a random number between 10 and 25 for the player and computer's attack strength.
- Create a function called `display_stats(player, computer)` which displays the `player` and `computer` `dict`s with nice formatted output.
- Create a `while` loop that:
    - Uses `display_stats()` to display the player/computer `dicts`
    - Prompts the user to press "Enter" to fight (we don't care about the return value from `input()` here)
    - Generates a random number between 1 and 2
    - If the random number is 1
        - Display "Computer attacks player!!!"
        - Decrease the player's health by the computer's attack strength
    - Otherwise
        - Display "Player attacks computer!!!"
        - Decrease the computer's health by the player's attack strength
    - If the player's health is 0 or less
        - Display "Player loses, computer wins!"
        - Exit the loop
    - If the computer's health is 0 or less
        - Display "Computer loses, player wins!"
        - Exit the loop


Example program output:

```text
Enter your username: djs

####################
Player stats: {'username': 'djs', 'health': 97, 'attack_strength': 18}
Computer stats: {'username': 'djs', 'health': 82, 'attack_strength': 19}
####################

Press enter to fight!
Computer attacks player!!!

####################
Player stats: {'username': 'djs', 'health': 78, 'attack_strength': 18}
Computer stats: {'username': 'djs', 'health': 82, 'attack_strength': 19}
####################

Press enter to fight!
Player attacks computer!!!

####################
Player stats: {'username': 'djs', 'health': 78, 'attack_strength': 18}
Computer stats: {'username': 'djs', 'health': 64, 'attack_strength': 19}
####################

Press enter to fight!
Computer attacks player!!!

####################
Player stats: {'username': 'djs', 'health': 59, 'attack_strength': 18}
Computer stats: {'username': 'djs', 'health': 64, 'attack_strength': 19}
####################

Press enter to fight!
Computer attacks player!!!

####################
Player stats: {'username': 'djs', 'health': 40, 'attack_strength': 18}
Computer stats: {'username': 'djs', 'health': 64, 'attack_strength': 19}
####################

Press enter to fight!
Player attacks computer!!!

####################
Player stats: {'username': 'djs', 'health': 40, 'attack_strength': 18}
Computer stats: {'username': 'djs', 'health': 46, 'attack_strength': 19}
####################

Press enter to fight!
Player attacks computer!!!

####################
Player stats: {'username': 'djs', 'health': 40, 'attack_strength': 18}
Computer stats: {'username': 'djs', 'health': 28, 'attack_strength': 19}
####################

Press enter to fight!
Player attacks computer!!!

####################
Player stats: {'username': 'djs', 'health': 40, 'attack_strength': 18}
Computer stats: {'username': 'djs', 'health': 10, 'attack_strength': 19}
####################

Press enter to fight!
Player attacks computer!!!
Computer loses, player wins!
```
