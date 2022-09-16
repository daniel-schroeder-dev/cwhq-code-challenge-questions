# 2022 Code Challenge - Question 04 

## Explanation

Sometimes, you'll want to build a `str` that mixes raw `str` data and the values
stored in variables. You can use `f-strings` to do this. An `f-string` starts with
the letter `f` and any variables inside `{}` are replaced with the value the variable
references.

```python
my_name = "Daniel"
my_age = 36

about_me = f"My name is {my_name} and I am {my_age} years old."
print(about_me)  # My name is Daniel and I am 36 years old.

# You can also print an `f-string` directly without creating a variable.
print(f"My name is {my_name} and I am {my_age} years old.")
```

## Exercise

Using what you learned in the *Explanation* section, create two variables:
- `favorite_book` which holds a `str` representing your favorite book
- `num_books` which holds an `int` representing the number of books you've read in the last 30 days.

Use `f-strings` to create and display a sentence like:
- "My favorite book is `___` and I've read `___` books in the last 30 days."

So, if your `favorite_book` is "The Hobbit" and you've read 3 books in the last 30 days, your output would be:
- "My favorite book is The Hobbit and I've read 3 books in the last 30 days."
