from data import data
import random


def find_opponents() -> list:
    opponent_list = []
    for i in range(2):
        opponent_list.append(random.choice(data))
    if opponent_list[0] == opponent_list[1]:
        while opponent_list[0] == opponent_list[1]:
            opponent_list[0] = random.choice(data)
    return opponent_list


def find_followers(array: list) -> list:
    follower_list = []
    for i in range(len(array)):
        follower_list.append(array[i]["follower_count"])
    return follower_list


def set_high_score(new_high_score):
    with open("score.txt", "r") as file:
        content = file.read()
    with open("score.txt", "w") as file:
        if new_high_score > int(content):
            file.write(str(new_high_score))


score = 0
players = find_opponents()
with open("score.txt", "r") as file:
    content = file.read()
print(f"High score: {content}")

while True:
    if find_followers(players)[0] > find_followers(players)[1]:
        players[1] = random.choice(data)
        if players[0] == players[1]:
            while players[0] == players[1]:
                players[1] = random.choice(data)
    else:
        players[0] = random.choice(data)
        if players[0] == players[1]:
            while players[0] == players[1]:
                players[0] = random.choice(data)
    print("-----------------------------------------------------------------------")
    print(f"Option A: {players[0]["name"]}, {players[0]["description"]}, {players[0]["country"]}")
    print("\nvs\n")
    print(f"Option B: {players[1]["name"]}, {players[1]["description"]}, {players[1]["country"]}")
    print("-----------------------------------------------------------------------")
    print(find_followers(players))
    choose = input("Who has more followers?: ").lower()
    if choose == "a":
        if find_followers(players)[0] > find_followers(players)[1]:
            score += 1
        else:
            print("\nYou lose.")
            print(f"Score: {score}")
            if score > int(content):
                print(f"New high score: {score}")
                set_high_score(score)
            break
    elif choose == "b":
        if find_followers(players)[0] < find_followers(players)[1]:
            score += 1
        else:
            print("\nYou lose.")
            print(f"Score: {score}")
            if score > int(content):
                print(f"New high score: {score}")
                set_high_score(score)
            break


