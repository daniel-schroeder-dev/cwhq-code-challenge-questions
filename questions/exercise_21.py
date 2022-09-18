from random import shuffle, choice


def display_deck(deck):
    for i, card in enumerate(deck):
        print(i, card)


def create_deck():
    suits = ["diamonds", "hearts"]

    deck = []
    for suit in suits:
        for rank in range(1, 5):
            card = {
                "suit": suit,
                "rank": rank,
            }
            deck.append(card)

    return deck


def take_cards(cards, deck):
    print("That's a match!")
    cards.append(first_card)
    cards.append(second_card)
    deck.remove(first_card)
    deck.remove(second_card)
    return cards


def display_cards(player_name, cards):
    print()
    print("#" * 20)
    print(f"{player_name}'s cards:")
    for card in cards:
        print(card)

    print("#" * 20)
    print()


deck = create_deck()
shuffle(deck)

player_cards = []
computer_cards = []

while True:
    # display_deck(deck)
    display_cards("Player", player_cards)
    display_cards("Computer", computer_cards)

    print(f"There are {len(deck)} cards left in the deck")

    first_index = int(input("Choose first card (by index): "))
    first_card = deck[first_index]
    print(f"Player chooses {first_card} at index {first_index}")

    second_index = int(input("Choose second card (by index): "))
    second_card = deck[second_index]
    print(f"Player chooses {second_card} at index {second_index}")

    if first_card["rank"] == second_card["rank"] and first_card != second_card:
        player_cards = take_cards(player_cards, deck)

    if len(deck) == 0:
        break

    first_card = choice(deck)
    first_index = deck.index(first_card)
    second_card = choice(deck)
    second_index = deck.index(second_card)

    print(f"Computer chooses {first_card} at index {first_index}")
    print(f"Computer chooses {second_card} at index {second_index}")

    if first_card["rank"] == second_card["rank"] and first_card != second_card:
        computer_cards = take_cards(computer_cards, deck)

    if len(deck) == 0:
        break


print("Final cards for each player")
display_cards("Player", player_cards)
display_cards("Computer", computer_cards)

if len(player_cards) > len(computer_cards):
    print("Player wins!")
elif len(computer_cards) > len(player_cards):
    print("Computer wins!")
else:
    print("It's a tie!")
