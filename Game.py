import random


def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    max_affordable = startingMoney // itemPrice

    if max_affordable < quantityToPurchase:
        quantity_purchased = max_affordable
    else:
        quantity_purchased = quantityToPurchase

    money_remaining = startingMoney - (quantity_purchased * itemPrice)

    return quantity_purchased, money_remaining


def new_random_monster():
    monster_type = random.randint(1, 3)

    if monster_type == 1:
        monster = {
            "name": "Cave Spider",
            "description": "A giant cave spider crawls out from behind a pile of rocks.",
            "health": random.randint(15, 35),
            "power": random.randint(5, 12),
            "money": random.randint(5, 30)
        }

    elif monster_type == 2:
        monster = {
            "name": "Skeleton Warrior",
            "description": "An old skeleton warrior rises from the ground and swings its rusty sword.",
            "health": random.randint(30, 60),
            "power": random.randint(10, 20),
            "money": random.randint(25, 75)
        }

    else:
        monster = {
            "name": "Mountain Troll",
            "description": "A huge mountain troll steps onto the trail and prepares to attack.",
            "health": random.randint(70, 120),
            "power": random.randint(20, 35),
            "money": random.randint(50, 150)
        }

    return monster


# Purchase 4 health potions that cost 25 each
num_purchased, leftover_money = purchase_item(25, 200, 4)
print("Health potions purchased:", num_purchased)
print("Money remaining:", leftover_money)


# Try to purchase 5 swords that cost 80 each
num_purchased, leftover_money = purchase_item(80, 250, 5)
print("Swords purchased:", num_purchased)
print("Money remaining:", leftover_money)


# Purchase 1 shield using the default quantity
num_purchased, leftover_money = purchase_item(60, 150)
print("Shields purchased:", num_purchased)
print("Money remaining:", leftover_money)


# Generate three random monsters

monster1 = new_random_monster()
print(monster1)

monster2 = new_random_monster()
print(monster2)
