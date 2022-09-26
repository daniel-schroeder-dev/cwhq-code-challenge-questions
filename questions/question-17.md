# 2022 Code Challenge - Question 17 - Using `for` Loops

## Explanation

You've learned a lot about `lists` in the last two exercises. Now, let's learn how to
use a different looping mechanism to loop through all of the items in a `list`.

Python's `for` loop allows you to loop through a `list`, one item at a time. Here
is the general syntax:

```python
friends = ["Django", "Lis", "Ryan", "Alex"]

# Note that `friend` is a variable name like any other. The convention
# in Python is to use the singular form of the list name for the loop
# variable, but you can name this variable whatever you like.
for friend in friends:
    print(friend)
```

*output*

```text
Django
Lis
Ryan
Alex
```

One thing that's nice about being able to loop through a `list` is that you can
loop through all items of one `list` and build another `list` from the original list.

Imagine you're working as a programmer for a big online shopping retailer like
Amazon. If there was a $1 off sale for all items in the store, you can imagine
that somewhere in Amazon's codebase there is logic similar to this:

```python
original_prices = [10, 5, 12, 4]
discounted_prices = []

print("Here are the original prices:")
for original_price in original_prices:
    print(f"${original_price}")

for original_price in original_prices:
    discounted_price = original_price - 1
    discounted_prices.append(discounted_price)


print("Here are the discounted prices:")
for discounted_price in discounted_prices:
    print(f"${discounted_price}")

```

*output*

```text
Here are the original prices:
$10
$5
$12
$4
Here are the discounted prices:
$9
$4
$11
$3
```

This technique is called a *mapping* between the lists.

## Exercise

Using what you've learned about looping through lists, create a program
that stores the ages of all the members in your household in a `list` 
and then uses the mapping technique to create a new list of all of the 
ages in 7 years. 

Hints:
- Create a `list` called `original_ages` that holds the original ages of each member of your household
- Create an empty `list` called `new_ages` that will hold the ages increased by 7 years
- Use a `for` loop to loop through the `original_ages` list and:
    - Create a variable to hold the `original_age` increased by 7 years
    - Add this variable to the `new_ages` list
- Display a message like: "Here are the original ages of all of the people in my household:"
- Loop through the `original_ages` list and display each age
- Display a message like: "Here are the ages of all of the people in my household increased by 7 years:"
- Loop through the `new_ages` list and display each age


Here's an example of how the program could work:

```text
Here are the original ages of all of the people in my household:
36
31
42
3
Here are the ages of all of the people in my household increased by 7 years:
43
38
49
10
```
