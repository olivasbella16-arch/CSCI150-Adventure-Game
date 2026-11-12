
"""Functions for a text-based adventure game.

This module handles the town menu, monster battles,
sleeping, shopping, and player actions.
"""

import random


def purchase_item(itemPrice, startingMoney, quantityToPurchase):
    """Calculate the number of items purchased and money remaining."""
    quantity = min(quantityToPurchase, startingMoney // itemPrice)
    moneyRemaining = startingMoney - (quantity * itemPrice)
    return int(quantity), moneyRemaining


def random_monster():
    """Generate a random monster with health and attack power."""
    monsters = ["Goblin", "Dragon", "Skeleton", "Wolf"]
    monster = random.choice(monsters)
    health = random.randint(10, 20)
    attack = random.randint(2, 5)
    return monster, health, attack


def print_welcome(name, width):
    """Print a centered welcome message for the player."""
    message = f"Hello, {name}!"
    print(f"{message:^{width}}")


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """Display a bordered shop menu with item names and prices."""
    print("/" + "-" * 22 + "\\")
    print(f"| {item1Name:<12} {f'${item1Price:.2f}':>8} |")
    print(f"| {item2Name:<12} {f'${item2Price:.2f}':>8} |")
    print("\\" + "-" * 22 + "/")


def get_menu_choice():
    """Display the town menu and validate the player's choice."""
    print("\nWhat would you like to do?")
    print("1) Leave town (Fight Monster)")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Quit")

    choice = input("Enter your choice: ")

    while choice not in ("1", "2", "3"):
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter your choice: ")

    return choice


def sleep(health, gold):
    """Restore the player's health in exchange for five gold."""
    if gold < 5:
        print("You do not have enough gold!")
    elif health >= 30:
        print("Your health is already full!")
    else:
        health = 30
        gold -= 5
        print("You slept and restored your health!")

    return health, gold


def get_fight_action():
    """Display the combat menu and validate the player's choice."""
    print("\nWhat would you like to do?")
    print("1) Attack")
    print("2) Run away")

    choice = input("Enter your choice: ")

    while choice not in ("1", "2"):
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice: ")

    return choice


def display_fight_statistics(health, monster_health):
    """Display the player's and monster's current health."""
    print("\nYour HP:", health)
    print("Monster HP:", monster_health)


def fight_monster(health, gold):
    """Run a monster battle until victory, defeat, or escape."""
    monster, monster_health, monster_attack = random_monster()
    print("\nA", monster, "appeared!")

    while health > 0 and monster_health > 0:
        display_fight_statistics(health, monster_health)
        action = get_fight_action()
        if action == "2":
            print("You ran away!")
            break
        monster_health -= 5
        if monster_health > 0:
            health -= monster_attack

    if health <= 0:
        health = 0
        print("You passed out!")
    elif monster_health <= 0:
        gold += 3
        print("You defeated the", monster, "and earned 3 gold!")

    return health, gold
