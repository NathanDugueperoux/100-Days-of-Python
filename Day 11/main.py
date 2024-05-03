import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []


def give_initial_decks():
    for i in range(2):
        player.append(random.choice(cards))
        dealer.append(random.choice(cards))


def calculate_score(deck: list):
    score = 0
    for i in deck:
        score += i
    return score


def check_win(p: list, d: list):
    p_score = calculate_score(p)
    d_score = calculate_score(d)
    if p_score > 21 and d_score > 21:
        print("You drew, both of you decks have a sum greater than 21.")
    elif p_score > 21:
        print("You lose, your cards have a sum greater than 21.")
    elif d_score > 21:
        print("You win, the dealers cards have a sum that exceeds 21.")
    elif d_score > p_score:
        print("You lose, the dealers cards have a sum greater than yours.")
    else:
        print("You win, your cards have a sum greater than the dealers.")


def check_ace(deck: list):
    for i in range(len(deck)):
        if deck[i] == 11:
            deck[i] = 1
            if calculate_score(deck) < 21:
                break


def check_dealer():
    if calculate_score(dealer) < 17:
        dealer.append(random.choice(cards))
        if calculate_score(dealer) > 21:
            check_ace(dealer)


while True:
    start = input("\nDo you want to play a game of Blackjack?: ").lower()
    if start == "no" or start == "n":
        break
    elif start == "yes" or start == "y":
        give_initial_decks()
        print(f"\nDealer: [{dealer[0]}, ##]\nTotal = {dealer[0]}\n\nPlayer: [{player[0]}, {player[1]}]\nTotal = {calculate_score(player)}\n")
        draw_card = input("Do you want to draw another card?: ").lower()
        if draw_card == "no" or draw_card == "n":
            check_dealer()
            if calculate_score(player) > 21:
                check_ace(player)
            print(f"\nDealer: {dealer}\nTotal = {calculate_score(dealer)}\n\nPlayer: [{player[0]}, {player[1]}]\nTotal = {calculate_score(player)}\n")
            check_win(player, dealer)
            player.clear()
            dealer.clear()
        elif draw_card == "yes" or draw_card == "y":
            player.append(random.choice(cards))
            if calculate_score(player) > 21:
                check_ace(player)
            if calculate_score(dealer) > 21:
                check_ace(dealer)
            print(f"\nDealer: {dealer}\nTotal = {calculate_score(dealer)}\n\nPlayer: {player}\nTotal = {calculate_score(player)}\n")
            check_win(player, dealer)
            player.clear()
            dealer.clear()