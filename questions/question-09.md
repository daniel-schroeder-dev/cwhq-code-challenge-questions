# 2022 Code Challenge - Question 09 

## Explanation

Sometimes, our programs need to make a decision based on more than one 
`True` or `False` (`bool`) condition. To do this, we use *Logical Operators*
and create *Complex Conditional Statements*. 

The `and` operator will evaluate an entire conditional expression to `True`
only if both expressions on either side of it are `True`. Otherwise, it
evaluates to `False`:

```python
age = 13
height = 5.6

 # True         # True
age > 12 and height > 5.5  # True

 # True         # False
age > 12 and height < 5.5  # False 

 # False        # False
age < 12 and height < 5.5  # False
```

The `or` operator will evaluate an entire conditional expression to `True`
if *any* expression on either side of it is `True`. It only evaluates to
`False` if *both* expressions are `False`:


```python
age = 13
height = 5.6

 # True         # True
age > 12 or height > 5.5  # True

 # True         # False
age > 12 or height < 5.5  # True 

 # False        # False
age < 12 or height < 5.5  # False
```

You use *Logical Operators* in *Complex Conditional Statements* like so:

```python
age = 13
height = 5.6

if age > 12 and height > 5.5:
    print("You can ride all of the rides at the carnival!")
else:
    print("Some rides will be off limits for you...")
```

## Exercise

Using what you've learned about *Logical Operators* and *Complex Conditional Statements*, create
a program that prompts a user for their resting heart rate (in beats-per-minute) and then
tells them their general heart health based on this table (note that these aren't exactly
medically accurate, but they are close enough for this project):

| Heart Health  | BPM Range |
|---------------|-----------|
| Athlete       | 50-55     |
| Excellent     | 56-61     |
| Great         | 62-68     |
| Good          | 69-72     |
| Average       | 73-77     |
| Below Average | 78-82     |
| Poor          | 83+       |

> Note: To calculate your resting heart rate, find your pulse and count the number of
> beats over a 30 second span and then double that number.

## Answer

```python
resting_heart_rate = int(input("Enter your resting heart rate (BPM): "))

heart_health = ""

if resting_heart_rate >= 78 and resting_heart_rate <= 82:
    heart_health = "Below Average"
elif resting_heart_rate >= 73 and resting_heart_rate <= 77:
    heart_health = "Average"
elif resting_heart_rate >= 69 and resting_heart_rate <= 72:
    heart_health = "Good"
elif resting_heart_rate >= 62 and resting_heart_rate <= 68:
    heart_health = "Great"
elif resting_heart_rate >= 56 and resting_heart_rate <= 61:
    heart_health = "Excellent"
elif resting_heart_rate >= 50 and resting_heart_rate <= 55:
    heart_health = "Athlete"
else:
    heart_health = "Poor"

print(f"Your heart health is {heart_health}.")
```
