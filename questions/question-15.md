# 2022 Code Challenge - Question 15 - Lists

## Explanation

So far, all of the variables in our program have referenced a single piece of
data (a `str` of text, a number, a `bool`). If we have related pieces of data, how
could we store all of them in one place?

Consider the example below, where we want to store the names of our friends in
variables:

```python
friend1 = "Django"
friend2 = "Lis"
friend3 = "Ryan"
friend4 = "Alex"
```

It's not obvious to the computer that all of those friends are related. The programmer
can tell because of the variable names, but then the programmer has to do all of the work
to keep track of those friends in a group. Programmers are lazy, and we want the computer
to keep track of things for us! 

Luckily, Python (and most programming languages) has built-in *Data Structures* that we can
use to hold multiple pieces of related data. The first *Data Structure* we'll look at is the
`list`. A `list` in Python (much like a real-world list) holds a sequence of related values
in a specific order. You create a `list` with the `[]` characters, like this:

```python
friends = ["Django", "Lis", "Ryan", "Alex"]
```

An alternative syntax for creating a `list` is:

```python
friends = [
    "Django",
    "Lis",
    "Ryan",
    "Alex",  # Note this trailing comma, it makes it easier to add items later!
]
```

The items in a `list` can be accessed altogether by printing the entire `list`:

```python
friends = ["Django", "Lis", "Ryan", "Alex"]
print(friends)  # ["Django", "Lis", "Ryan", "Alex"]
```

If you want to access `list` items one at a time, you can use the index number of the item. 
The index numbers start at 0, so the `friends` `list` from above would have the following index numbers:

```python
friends = ["Django", "Lis", "Ryan", "Alex"]
          #   0        1      2       3
```

To access items individually in our `friends` `list`, we use the `[]` notation and the index number:

```python
friend1 = friends[0]
print(friend1)  # Django

friend2 = friends[1]
print(friend2)  # Lis
```

If you want to know how many items are in your `list`, you can use a built-in Python function
called `len()`:

```python
friends = ["Django", "Lis", "Ryan", "Alex"]
num_friends = len(friends)

print(f"There are {num_friends} friends in my friends list.")  # There are 4 friends in my friends list.
```

There are many more interesting things you can do with a `list`, but that's enough for now!

## Further Reading

If you're interested in more information on `lists`, see these resources:
-   [CWHQ Docs - `list`](https://docs.codewizardshq.com/python/python-language/#list)
-   [The Python Tutorial - Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
-   [Think Python - Lists](https://greenteapress.com/thinkpython2/html/thinkpython2011.html)


## Exercise

Using what you've learned about the `list` data structure, create a `list` of the top 5 programming
languages from the [TIOBE index](https://www.tiobe.com/tiobe-index/) and display a nice output of them.

Hints:

- You can call this `list` something like `programming_languages`.
- Get the length of the `list` and store it in a variable called `num_programming_languages`.
    - Make sure to use a function to do this!
- Display a header like: "These are the top [num_programming_languages] programming languages for October 2022:" 
- Display each programming language along with it's ranking one-by-one
    - You can pull each programming language into its own variable or print them directly using the index number, 
    but make sure to use index numbers in this portion no matter what!

Here's an example of how the program output might look:

```text
These are the top 5 programming languages for October 2022:
1: Python
2: C
3: Java
4: C++
5: C#
```
