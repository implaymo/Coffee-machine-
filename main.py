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


def machine_question():
    """ Questions the user what type they want. Exits the program and shows report """
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Stops program or shows report of the bill and items
    return question


def calculator():
    """Prompts the user and gives Change"""
    # Price of Items
    espresso_price = MENU["espresso"]["cost"]
    latte_price = MENU["latte"]["cost"]
    cappuccino_price = MENU["cappuccino"]["cost"]
    money_spent = 0

    # Prompts the user
    game_live = True
    while game_live:
        drink_choice = machine_question()
        print("Please insert coin.")

        # LATTE
        if drink_choice == "latte":
            # Reduces ingredients to resources
            for i in MENU[drink_choice]["ingredients"]:
                resources[i] -= MENU[drink_choice]["ingredients"][i]
                if resources[i] < 0:
                    print(f"Sorry there is no {i}.")
                    exit()
            total_cash = coins_cash()
            money_spent += latte_price
            # Gives change if user has more cash
            change = round(total_cash - latte_price, 2)
            if change < 0:
                print("You dont have enough money. Money refunded")
            else:
                print(f"Here is ${change} in change")
                print(f"Here is your latte ☕")

        # CAPPUCCINO
        elif drink_choice == "cappuccino":
            # Reduces ingredients to resources
            for i in MENU[drink_choice]["ingredients"]:
                resources[i] -= MENU[drink_choice]["ingredients"][i]
                if resources[i] < 0:
                    print(f"Sorry there is no {i}.")
                    exit()
            total_cash = coins_cash()
            money_spent += cappuccino_price
            # Gives change if user has more cash
            change = round(total_cash - cappuccino_price, 2)
            if change < 0:
                print("You dont have enough money. Money refunded")
            else:
                print(f"Here is ${change} in change")
                print(f"Here is your cappuccino ☕")

        # EXPRESSO
        elif drink_choice == "espresso":
            # Reduces ingredients to resources
            for i in MENU[drink_choice]["ingredients"]:
                resources[i] -= MENU[drink_choice]["ingredients"][i]
                if resources[i] < 0:
                    print(f"Sorry there is no {i}.")
                    exit()
            total_cash = coins_cash()
            money_spent += espresso_price
            change = round(total_cash - espresso_price, 2)
            if change < 0:
                print("You dont have enough money. Money refunded")
            else:
                print(f"Here is ${change} in change")
                print(f"Here is your espresso ☕")

        # Ends program
        elif drink_choice == "off":
            exit()
        # Gets the report of the resources and the money spent
        elif drink_choice == "report":
            # Gets the amount of resources and money spent
            for resource, value in resources.items():
                if resource == "water" or resource == "milk":
                    print(f"{resource}: {value}ml")
                else:
                    print(f"{resource}: {value}g")
            print(f"Money: ${money_spent}")


def coins_cash():
    """Prompt user for coins and gets the total cash"""
    total_quarters = float(input("How many quarters?: "))
    total_dimes = float(input("How many dimes?: "))
    total_nickles = float(input("How many nickles?: "))
    total_pennies = float(input("How many pennies?: "))

    # Type of coins
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    total_cash = ((total_quarters * quarters) + (total_dimes * dimes) + (total_nickles * nickles) +
                  (total_pennies * pennies))

    return total_cash


def main():
    # Create a loop to keep asking for coffee till user doesn't want anything
    machine_working = True
    while machine_working:
        # Prompt user for amount of coins and type they have
        calculator()


main()
