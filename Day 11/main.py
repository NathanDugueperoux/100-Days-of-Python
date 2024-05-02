import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []

while True:
    start = input("Do you want to play a game of Blackjack?: ").lower()
    if start == "no" or start == "n":
        break
    elif start == "yes" or start == "y":
        for i in range(2):
            player.append(random.choice(cards))
            dealer.append(random.choice(cards))

        print(f"\nDealers hand: [{dealer[0]}, ##]\nTotal = {dealer[0]}\n\nPlayers hand: [{player[0]}, {player[1]}]\nTotal = {player[0]+player[1]}\n")

        take_card = input("Do you wish to take another card?:").lower()
        if take_card == "no" or take_card == "n":
            if (dealer[0]+dealer[1]) > 17:
                print("Since dealers sum of cards is less than 17, Dealer must take another card.")
                dealer.append(random.choice(cards))
                if (dealer[0]+dealer[1]+dealer[2]) > 21 and 11 in dealer:
                    for i in range(len(dealer)):
                        if dealer[i] == 11:
                            dealer[i] = 1
                            if (dealer[0]+dealer[1]+dealer[2]) < 21:
                                pass
                elif (dealer[0]+dealer[1]+dealer[2]) > 21 and 11 not in dealer:
                    print(f"\nDealers hand: [{dealer[0]}, {dealer[1]}, {dealer[2]}]\nTotal = {dealer[0]+dealer[1]+dealer[2]}\n\nPlayers hand: [{player[0]}, {player[1]}]\nTotal = {player[0]+player[1]}\n")
            else:
                pass
