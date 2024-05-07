MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_report():
    print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: {resources["money"]}")


def make_drink(choice: str):
    if choice == "espresso":
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    else:
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]


def handle_money(choice):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    if total > MENU[choice]["cost"]:
        total -= MENU[choice]["cost"]
        resources["money"] += MENU[choice]["cost"]
        return float(total)

    else:
        return False


while True:
    choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose == "report":
        print_report()
    elif choose == "espresso":
        make_drink(choose)
        if not handle_money(choose):
            print("Not enough money. Money Refunded.")

    elif choose == "latte":
        make_drink(choose)
        if not handle_money(choose):
            print("Not enough money. Money Refunded.")
    elif choose == "cappuccino":
        make_drink(choose)
        if not handle_money(choose):
            print("Not enough money. Money Refunded.")
        elif handle_money(choose) == float:
            print("Here's your drink.")
    else:
        print("Not an option.")