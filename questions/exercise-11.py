from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)
num_guesses = 0
total = num1 + num2

print(f"The sum of the numbers is: {total}")

while True:
    user_guess1 = int(input("What do you think the first number is? "))
    user_guess2 = int(input("What do you think the second number is? "))
    num_guesses = num_guesses + 1

    if user_guess1 == num1 and user_guess2 == num2:
        print("That's correct!")
        print(f"The numbers were {num1} + {num2} = {total}")
        break
    else:
        print("That's incorrect, try again!")

print(f"It took you {num_guesses} guesses to get the correct answer.")
