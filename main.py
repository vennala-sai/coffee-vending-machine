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
}

def check_resources_sufficient(order):
    for k in MENU[order]["ingredients"]:
        if k in resources:
            if resources[k] - MENU[order]["ingredients"][k] < 0:
                return False, f"Sorry there is not enough {k}"
            else:
                return True, "Sure, I can make that!"

def subtract_resources(order):
    for k in MENU[order]["ingredients"]:
        if k in resources:
            resources[k] = resources[k] - MENU[order]["ingredients"][k]



def coffee_machine():
    order = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()

    def price_calculator(total):
        return total - MENU[order]["cost"]
    if order == "off":
        exit()
    elif order == "report":
        print(resources)
    else:
        proceed, result = check_resources_sufficient(order)
        print(result)
        if proceed:
            print(f"Please insert coins. The total cost is: ${MENU[order]['cost']}")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total = quarters * 0.25 + dimes * 0.10 + nickels * 0.5 + pennies * 0.1

            if total == MENU[order]["cost"]:
                subtract_resources(order)
                print(f"Here is your {order} enjoy!!!")
            elif total < MENU[order]["cost"]:
                print("Not enough money!!!!")
            else:
               subtract_resources(order)
               remaining = price_calculator(total)
               print(f"Here is your ${remaining} change. Enjoy!")

    if input("Do you like to order more? Type 'y' or 'n': ").lower() == 'y':
        coffee_machine()


coffee_machine()