# 2022 Code Challenge - Question 20 - Dictionary Methods

## Explanation

Just like `lists`, `dicts` have *methods* attached to them to perform certain common tasks. We'll
look at two `dict` methods: `dict.pop()` and `dict.items()`.

The `dict.pop()` method allows you to remove a key/value pair from a `dict`. It returns the value
of a given key:

```python
user = {
    "username": "danielj",
    "role": "Curriculum Developer",
    "is_active": True,
    "year_joined": 2020,
}

year_joined = user.pop("year_joined")

print(user)
print(f"The user joined in {year_joined}")
```

*output*

```text
{
    "username": "danielj",
    "role": "Curriculum Developer",
    "is_active": True,
}
The user joined in 2020
```

The `dict.items()` method allows you to loop through the key/value pairs of a `dict` in a `for` loop:

```python
user = {
    "username": "danielj",
    "role": "Curriculum Developer",
    "is_active": True,
    "year_joined": 2020,
}

for key, value in user.items():
    print(f"{key} -> {value}")

```

*output*

```text
username -> danielj
role -> Curriculum Developer
is_active -> True
year_joined -> 2020
```


## Exercise

Using what you've learned about the `dict.pop()` and `dict.items()` methods, create a program
that models a library using a `dict`. Each key/value pair will refer to authors/titles of books, 
and users should be able to add, update, and remove books from the underlying `library` `dict`.

Hints:
- Create an empty `dict` called `library` to hold the author/title key/value pairs
- Create a function called `display_books(library)` that loops through all of the key/value
pairs in `library` and displays the author/title of each book in a formatted way.
- Create a multiline string of `options` for the user to choose from:
    1. Add a book
    2. Update a book
    3. Remove a book
    4. Exit
- In a `while` loop:
    - Use `display_books()` to display the `library`
    - Prompt the user for their choice from the `options`
    - If the user chooses to add or update a book
        - Prompt the user for the book title
        - Prompt the user for the author
        - Add or update the `library` with the title/author key/value pair
    - If the user chooses to remove a book
        - Prompt the user for the book title to remove
        - Remove the book from the library and store the author of the removed title
        - Display a message like: "Removed [title] by [author]"
    - If the user chooses to exit
        - Display a message like: "Goodbye!"
        - Exit the loop

Example program output:

```text
Current Library Books:

####################
####################

    Welcome to the Library!

    1.) Add a book
    2.) Update a book
    3.) Remove a book
    4.) Exit
1
Enter book title: The Fellowship of the Ring
Enter author name: J. Tolkien

Current Library Books:

####################

Title: The Fellowship of the Ring
Author: J. Tolkien

####################

    Welcome to the Library!

    1.) Add a book
    2.) Update a book
    3.) Remove a book
    4.) Exit
1
Enter book title: The Grapes of Wrath
Enter author name: John Steinbeck

Current Library Books:

####################

Title: The Fellowship of the Ring
Author: J. Tolkien


Title: The Grapes of Wrath
Author: John Steinbeck

####################

    Welcome to the Library!

    1.) Add a book
    2.) Update a book
    3.) Remove a book
    4.) Exit
2
Enter book title: The Fellowship of the Ring
Enter author name: J.R.R. Tolkien

Current Library Books:

####################

Title: The Fellowship of the Ring
Author: J.R.R. Tolkien


Title: The Grapes of Wrath
Author: John Steinbeck

####################

    Welcome to the Library!

    1.) Add a book
    2.) Update a book
    3.) Remove a book
    4.) Exit
3
Enter book title to remove: The Grapes of Wrath
Removed The Grapes of Wrath by John Steinbeck

Current Library Books:

####################

Title: The Fellowship of the Ring
Author: J.R.R. Tolkien

####################

    Welcome to the Library!

    1.) Add a book
    2.) Update a book
    3.) Remove a book
    4.) Exit
4
Goodbye!
```
