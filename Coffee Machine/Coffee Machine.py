MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Milk": 0,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

PENNY = 0.01
DIME = 0.10
NICKEL = 0.05
QUARTER = 0.25

def print_resources():
    for key in resources:
        if key == "Water" or key == "Milk":
            print(f"{key}: {resources[key]}ml")
        elif key == "Coffee":
            print(f"{key}: {resources[key]}g")
    money = resources["Money"]
    print(f"Money: ${money}")

def check_enough_resources(selected_coffee_type):
    if selected_coffee_type == 'latte' or selected_coffee_type == 'cappuccino':
        if MENU[selected_coffee_type]["ingredients"]["Water"] > resources["Water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU[selected_coffee_type]["ingredients"]["Milk"] > resources["Milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif MENU[selected_coffee_type]["ingredients"]["Coffee"] > resources["Coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    elif selected_coffee_type == 'espresso':
        if MENU[selected_coffee_type]["ingredients"]["Water"] > resources["Water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU[selected_coffee_type]["ingredients"]["Coffee"] > resources["Coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

def check_enough_money(selected_coffee_type, no_quarters, no_of_dimes, no_of_nickles, no_of_pennies):
    amount = 0
    total_paid = no_quarters * QUARTER + no_of_dimes * DIME + no_of_nickles * NICKEL + no_of_pennies * PENNY
    for each_coffee_type in MENU:
        if selected_coffee_type == each_coffee_type:
            amount = MENU[each_coffee_type]["cost"]
            if total_paid < amount:
                print("Sorry that's not enough money. Money refunded.")
                return False
            else:
                balance = total_paid - amount
                print(f"Here is ${round(balance, 2)} in change.\nHere is your {selected_coffee_type} ☕. Enjoy!")
                return True

def update_resources(selected_coffee_type):
    for each_coffee_type in MENU:
        if selected_coffee_type == each_coffee_type:
            resources["Water"] -= MENU[each_coffee_type]["ingredients"]["Water"]
            resources["Milk"] -= MENU[each_coffee_type]["ingredients"]["Milk"]
            resources["Coffee"] -= MENU[each_coffee_type]["ingredients"]["Coffee"]
            resources["Money"] += MENU[each_coffee_type]["cost"]

status = 'on'
continue_operation = True

while status == 'on':
    while True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if coffee_type == 'off':
            status = 'off'
            break

        if coffee_type == 'report':
            print_resources()

        if coffee_type == 'espresso' or coffee_type == 'latte' or coffee_type == 'cappuccino':
            has_resources = check_enough_resources(coffee_type)
            if has_resources is False:
                continue_operation = False

            else:
                print("Please insert coins.")
                quarters = int(input('How many quarters? '))
                dimes = int(input('How many dimes? '))
                nickles = int(input('How many nickles? '))
                pennies = int(input('How many pennies? '))
                has_enough_money = check_enough_money(coffee_type, quarters, dimes, nickles, pennies)
                if has_enough_money is True and has_resources is True:
                    update_resources(coffee_type)
