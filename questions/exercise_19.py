from random import randint


def display_stats(player, computer):
    print()
    print("#" * 20)
    print(f"Player stats: {player}")
    print(f"Computer stats: {computer}")
    print("#" * 20)
    print()


username = input("Enter your username: ")
player_health = randint(50, 100)
player_attack_strength = randint(10, 25)

player = {
    "username": username,
    "health": player_health,
    "attack_strength": player_attack_strength,
}


computer_health = randint(50, 100)
computer_attack_strength = randint(10, 25)

computer = {
    "username": username,
    "health": computer_health,
    "attack_strength": computer_attack_strength,
}

while True:
    display_stats(player, computer)
    input("Press enter to fight!")

    random_number = randint(1, 2)
    if random_number == 1:
        print("Computer attacks player!!!")
        player["health"] -= computer["attack_strength"]
    else:
        print("Player attacks computer!!!")
        computer["health"] -= player["attack_strength"]

    if player["health"] <= 0:
        print("Player loses, computer wins!")
        break
    elif computer["health"] <= 0:
        print("Computer loses, player wins!")
        break


