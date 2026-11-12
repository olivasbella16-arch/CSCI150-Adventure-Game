
"""Run a simple interactive adventure game."""

import gamefunctions


def main():
    """Welcome the player and begin an adventure."""
    print("WELCOME TO THE ADVENTURE GAME!")

    name = input("What is your name? ")
    gamefunctions.print_welcome(name, 40)

    print("\nYou are beginning your adventure!")
    print("You have $100 to spend in the shop.")

    money = 100

    print("\nWelcome to the Adventure Shop!")
    gamefunctions.print_shop_menu("Sword", 25, "Potion", 10)

    choice = input("\nWould you like a sword or potion? ")
    choice = choice.lower()

    if choice == "sword":
        item_price = 25
    elif choice == "potion":
        item_price = 10
    else:
        print("Invalid choice. No item purchased.")
        item_price = 0

    if item_price > 0:
        quantity = int(input("How many would you like? "))

        purchased, money = gamefunctions.purchase_item(
            item_price, money, quantity
        )

        print("Items purchased:", purchased)
        print("Money remaining: $", money)

    print("\nYou leave the shop and enter a dark forest...")

    monster, health, attack = gamefunctions.random_monster()

    print("\nA wild", monster, "appears!")
    print("Monster health:", health)
    print("Monster attack power:", attack)

    action = input("\nWould you like to fight or run? ")
    action = action.lower()

    if action == "fight":
        print("You bravely prepare to fight the", monster + "!")
    elif action == "run":
        print("You escape safely from the", monster + "!")
    else:
        print("You hesitate as the monster approaches!")

    print("\nThank you for playing,", name + "!")


if __name__ == "__main__":
    main()
