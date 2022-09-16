from random import randint


def check_die(score, die_value):
    if die_value == 1:
        return 0
    else:
        return score + die_value


def display_scoreboard(player_score, computer_score):
    print()
    print("#" * 20)
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("#" * 20)
    print()


player_score = 0
computer_score = 1

while True:
    input("Press 'Enter' to roll the die...\n")
    die_value = randint(1, 6)
    print(f"Player rolls a {die_value}")
    player_score = check_die(player_score, die_value)

    die_value = randint(1, 6)
    print(f"Computer rolls a {die_value}")
    computer_score = check_die(computer_score, die_value)

    display_scoreboard(player_score, computer_score)

    if player_score >= 30:
        print("Player wins!")
        break
    elif computer_score >= 30:
        print("Computer wins!")
        break
        


