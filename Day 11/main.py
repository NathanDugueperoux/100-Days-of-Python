import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []

while True:
    start = input("Do you want to play a game of Blackjack?: ").lower()
    if start == "no" or "n":
        break
    elif start == "yes" or "y":
        for i in range(2):
            player.append(random.choice(cards))
            dealer.append(random.choice(cards))

        if player[0] == 11 and player[1] == 11:
            player[0] = 1
        if dealer[0] == 11 and dealer[1] == 11:
            dealer[0] = 1

        print(f"\nDealers hand: [{dealer[0]}, ##]\nTotal = {dealer[0]}\n\nPlayers hand: [{player[0]}, {player[1]}]\nTotal = {player[0]+player[1]}\n")

        take_card = input("Do you wish to take another card?:").lower()
        if take_card == "no" or take_card == "n":
            if (dealer[0]+dealer[1]) > 17:
                print("Since dealers sum of cards is less than 17, Dealer must take another card.")
                dealer.append(random.choice(cards))
                if (dealer[0]+dealer[1]+dealer[2]) > 21 and 11 in dealer:
                    while True:
                        for i in range(len(dealer)):
                            if dealer[i] == 11:
                                dealer[i] = 1
                                if (dealer[0]+dealer[1]+dealer[2]) < 21:
                                    break
                                elif 11 not in dealer:
                                    break
                                else:
                                    pass
                if ((dealer[0]+dealer[1]+dealer[2]) > 21 and 11 not in dealer) and (player[0]+player[1]) < 21:
                    print(f"\nDealers hand: [{dealer[0]}, {dealer[1]}, {dealer[2]}]\nTotal = {dealer[0]+dealer[1]+dealer[2]}\n\nPlayers hand: [{player[0]}, {player[1]}]\nTotal = {player[0]+player[1]}\n")
                    print("You win, Dealers sum exceeds 21")
                elif ((dealer[0] + dealer[1] + dealer[2]) > 21 and 11 not in dealer) and (player[0] + player[1]) > 21:
                    print(f"\nDealers hand: [{dealer[0]}, {dealer[1]}, {dealer[2]}]\nTotal = {dealer[0]+dealer[1]+dealer[2]}\n\nPlayers hand: [{player[0]}, {player[1]}]\nTotal = {player[0] + player[1]}\n")
                    print("You drew, both your sums exceed 21")
                elif ((dealer[0] + dealer[1] + dealer[2]) < 21) and (player[0] + player[1]) > 21:
                    print(f"\nDealers hand: [{dealer[0]}, {dealer[1]}, {dealer[2]}]\nTotal = {dealer[0] + dealer[1] + dealer[2]}\n\nPlayers hand: [{player[0]}, {player[1]}]\nTotal = {player[0] + player[1]}\n")
                    print("You lost, your sum exceeds 21")
                elif ((dealer[0] + dealer[1] + dealer[2]) < 21) and (player[0] + player[1]) < 21:
                    if (dealer[0] + dealer[1] + dealer[2]) > (player[0] + player[1]):
                        print(f"\nDealers hand: [{dealer[0]}, {dealer[1]}, {dealer[2]}]\nTotal = {dealer[0] + dealer[1] + dealer[2]}\n\nPlayers hand: [{player[0]}, {player[1]}]\nTotal = {player[0] + player[1]}\n")
                        print("Dealer wins.")
                    else:
                        print(f"\nDealers hand: [{dealer[0]}, {dealer[1]}, {dealer[2]}]\nTotal = {dealer[0] + dealer[1] + dealer[2]}\n\nPlayers hand: [{player[0]}, {player[1]}]\nTotal = {player[0] + player[1]}\n")
                        print("Player wins.")
            else:
                pass