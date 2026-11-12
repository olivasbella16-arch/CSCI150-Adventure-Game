"""Provide functions for a text-based adventure game.

This module contains functions for welcoming players, displaying
shop menus, purchasing items, and generating random monsters.

The functions can be imported into game.py or tested directly.
The random module is used to generate monsters and their stats.
"""

import random


def purchase_item(itemPrice, startingMoney, quantityToPurchase):
    """Calculate the number of items purchased and money remaining.

    Args:
        itemPrice (int): The price of one item.
        startingMoney (int): The player's available money.
        quantityToPurchase (int): The number of items requested.

    Returns:
        tuple: The quantity purchased and money remaining.
    """
    quantity = min(quantityToPurchase, startingMoney // itemPrice)
    moneyRemaining = startingMoney - (quantity * itemPrice)
    return int(quantity), moneyRemaining


def random_monster():
    """Generate a random monster with health and attack power.

    Returns:
        tuple: The monster name, health, and attack power.
    """
    monsters = ["Goblin", "Dragon", "Skeleton", "Wolf"]
    monster = random.choice(monsters)
    health = random.randint(50, 150)
    attack = random.randint(5, 25)
    return monster, health, attack


def print_welcome(name, width):
    """Print a centered welcome message for the player.

    Args:
        name (str): The name of the player.
        width (int): The width used to center the message.

    Returns:
        None: This function prints a message.
    """
    message = f"Hello, {name}!"
    print(f"{message:^{width}}")


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """Display a bordered shop menu with item names and prices.

    Args:
        item1Name (str): The name of the first item.
        item1Price (float): The price of the first item.
        item2Name (str): The name of the second item.
        item2Price (float): The price of the second item.

    Returns:
        None: This function prints the shop menu.
    """
    print("/" + "-" * 22 + "\\")
    print(f"| {item1Name:<12} {f'${item1Price:.2f}':>8} |")
    print(f"| {item2Name:<12} {f'${item2Price:.2f}':>8} |")
    print("\\" + "-" * 22 + "/")


def test_functions():
    """Test all four adventure game functions."""
    # Test purchase_item() three times
    print("PURCHASE ITEM TESTS")

    print(purchase_item(15, 100, 3))
    print(purchase_item(25, 60, 4))
    print(purchase_item(8, 50, 5))

    # Test random_monster() three times
    print("\nRANDOM MONSTER TESTS")

    print(random_monster())
    print(random_monster())
    print(random_monster())

    # Test print_welcome() three times
    print("\nWELCOME MESSAGE TESTS")

    print_welcome("Bella", 20)
    print_welcome("Alexander", 30)
    print_welcome("Max", 25)

    # Test print_shop_menu() three times
    print("\nSHOP MENU TESTS")

    print_shop_menu("Sword", 25, "Shield", 18.5)
    print()
    print_shop_menu("Potion", 3.456, "Magic Staff", 125)
    print()
    print_shop_menu("Arrow", 0.5, "Health Pack", 12.999)


if __name__ == "__main__":
    test_functions()

