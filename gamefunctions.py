
import random


def purchase_item(itemPrice, startingMoney, quantityToPurchase):
    """Calculate how many items can be purchased and money remaining."""
    quantity = min(quantityToPurchase, startingMoney // itemPrice)
    moneyRemaining = startingMoney - (quantity * itemPrice)
    return int(quantity), moneyRemaining


def new_random_monster():
    """Generate a random monster with a name, health, and attack power."""
    monsters = ["Goblin", "Dragon", "Skeleton", "Wolf"]
    monster = random.choice(monsters)
    health = random.randint(50, 150)
    attack = random.randint(5, 25)
    return monster, health, attack


def print_welcome(name, width):
    """Print a centered welcome message within the specified width."""
    message = f"Hello, {name}!"
    print(f"{message:^{width}}")


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """Print a bordered shop menu with aligned items and prices."""
    print("/" + "-" * 22 + "\\")
    print(f"| {item1Name:<12} {f'${item1Price:.2f}':>8} |")
    print(f"| {item2Name:<12} {f'${item2Price:.2f}':>8} |")
    print("\\" + "-" * 22 + "/")


# Test purchase_item() three times
print("PURCHASE ITEM TESTS")

print(purchase_item(15, 100, 3))
print(purchase_item(25, 60, 4))
print(purchase_item(8, 50, 5))


# Test new_random_monster() three times
print("\nRANDOM MONSTER TESTS")

print(new_random_monster())
print(new_random_monster())
print(new_random_monster())


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
