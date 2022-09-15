from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)
total = num1 + num2

print(num1, num2)

print(f"The sum of the numbers is: {total}")

user_guess1 = int(input("What do you think the first number is? "))
user_guess2 = int(input("What do you think the second number is? "))

if user_guess1 == num1 and user_guess2 == num2:
    print("That's correct! You win $100.")
else:
    print("Sorry, better luck next time!")

print(f"The numbers were {num1} + {num2} = {total}")
