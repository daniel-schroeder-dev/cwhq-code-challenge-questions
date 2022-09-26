# 2022 Code Challenge - Question 16 - List Methods

## Explanation

Besides creating a `list` and pulling items from it, you can also add, remove, and update items in a `list`.
The easiest way to add or remove items from a `list` is to use the built-in `list` *methods*. A method is a
special type of function that exists on a particular data structure. You can see some of the common `list`
methods here [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
and here [Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types). 
When you see something in the form `data_structure.method_name()`, the function after the `.` is a method.

Here are two `list` methods for adding or removing items from a `list`:

```python
friends = ["Django", "Lis", "Ryan", "Alex"]

# The `list.append()` method adds an item to a `list`
friends.append("Sam")
print(friends)  # ["Django", "Lis", "Ryan", "Alex", "Sam"]

# The `list.pop(index_number)` method removes an item at `index_number` from a `list`
# The item removed from the `list` is returned so you can capture it in a variable if you wish
removed_friend = friends.pop(0)

print(f"Removed {removed_friend} from the friends list.") # Removed Django from the friends list.
print(friends)  # ["Lis", "Ryan", "Alex", "Sam"] 
```

To update an item in a `list`, you can use the same techniques you learned in the previous exercise for
accessing a `list` item:

```python
friends = ["Django", "Lis", "Ryan", "Alex"]

# Updating the friend at index 3
friends[3] = "Sherri"
print(friends)  # ["Django", "Lis", "Ryan", "Sherri"]
```

## Further Reading

If you're interested in more information about `lists`, see these resources:
-   [CWHQ Docs - `list`](https://docs.codewizardshq.com/python/python-language/#list)
-   [The Python Library Reference - Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
-   [The Python Library Reference - Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
-   [The Python Library Reference - `len()`](https://docs.python.org/3/library/functions.html#len)
-   [The Python Tutorial - Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
-   [Think Python - Lists](https://greenteapress.com/thinkpython2/html/thinkpython2011.html)

## Exercise

Using what you've learned about adding, removing, and updating items in a `list`, create a program
that allows users to add, remove, and update items in a virtual shopping cart.

Hints:
- Create an empty `list` called `shopping_cart`
- In a `while` loop:
    - Display the `shopping_cart` `list` with a message like: "Here's your current shopping cart: [shopping_cart]"
    - Prompt the user with the following options (they will enter a number between 1 and 4 to choose an option):
        1. Add item to shopping cart
        2. Update item in shopping cart
        3. Remove item from shopping cart
        4. Exit
    - If the user chooses to add an item to the shopping cart
        - Prompt them for the item name to add
        - Add the item to the `shopping_cart` `list`
    - If the user chooses to update an item in the shopping cart
        - Prompt them for the item index to update
        - Prompt them for the new item name
        - Update the item in the `shopping_cart` at the given index with the new item name
    - If the user chooses to remove an item in the shopping cart
        - Prompt them for the index of the item to remove
        - Remove the item from the `shopping_cart` and store it in a variable
        - Display a message like: "Removed [item_name] from your shopping cart
    - If the user chooses to exit the program
        - Display a message like: "Goodbye!"
        - Exit the loop

> Note, with larger prompts like the one above, you may want to create a multiline
> string with all of the options and print that, as in the example below:

```python
options = """
    Choose one of the following options:
    1.) Eat a burrito
    2.) Eat a taco
    3.) Eat nachos
    4.) Exit
"""

user_choice = int(input(options))
```

Here's an example of how the program could work:

```text
Here's your current shopping cart: []

    What would you like to do?

    1.) Add an item to the shopping cart
    2.) Update an item in the shopping cart
    3.) Remove an item from the shopping cart
    4.) Exit
1
What item would you like to add? PlayStation7
Here's your current shopping cart: ['PlayStation7']

    What would you like to do?

    1.) Add an item to the shopping cart
    2.) Update an item in the shopping cart
    3.) Remove an item from the shopping cart
    4.) Exit
1
What item would you like to add? MacBook9000
Here's your current shopping cart: ['PlayStation7', 'MacBook9000']

    What would you like to do?

    1.) Add an item to the shopping cart
    2.) Update an item in the shopping cart
    3.) Remove an item from the shopping cart
    4.) Exit
2
What is the index number of the item you want to update? 0
What is the new item name you want to use? XBox20
Here's your current shopping cart: ['XBox20', 'MacBook9000']

    What would you like to do?

    1.) Add an item to the shopping cart
    2.) Update an item in the shopping cart
    3.) Remove an item from the shopping cart
    4.) Exit
3
What is the index number of the item you want to remove? 1
Removed MacBook9000 from your shopping cart.
Here's your current shopping cart: ['XBox20']

    What would you like to do?

    1.) Add an item to the shopping cart
    2.) Update an item in the shopping cart
    3.) Remove an item from the shopping cart
    4.) Exit
4
Goodbye!
```

