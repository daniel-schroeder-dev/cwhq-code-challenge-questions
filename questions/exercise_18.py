from random import randint


def display_scoreboard(player_score, computer_score):
    print()
    print("#" * 20)
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("#" * 20)
    print()


def calculate_score(name):
    score = 0
    for num in range(5):
        die_amount = randint(1, 6)
        print(f"{name} rolls {die_amount}")
        if die_amount != 3:
            score += die_amount
    return score


player_score = 0
computer_score = 0

while True:
    display_scoreboard(player_score, computer_score)

    input("Press `Enter` to play this round:")
    player_score += calculate_score("Player")
    computer_score += calculate_score("Computer")

    if player_score >= 100:
        print("Player loses, computer wins!")
        break
    elif computer_score >= 100:
        print("Computer loses, player wins!")
        break
    
