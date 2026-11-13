
"""Helper functions for the text-based adventure game."""

import random


def print_welcome(name, width):
    """Display a centered welcome message."""
    print(f"{'Hello, ' + name + '!':^{width}}")


def random_monster():
    """Generate a random monster."""
    monsters = ["Goblin", "Dragon", "Skeleton", "Wolf"]
    return random.choice(monsters), random.randint(10, 20), random.randint(2, 5)


def get_choice(prompt, choices):
    """Validate user input."""
    choice = input(prompt).strip()
    while choice not in choices:
        print("Invalid choice. Please try again.")
        choice = input(prompt).strip()
    return choice


def town_menu(state):
    """Display the town menu."""
    print(f"\nYou are in town. HP: {state['player_hp']}/{state['max_hp']}  Gold: {state['player_gold']}")
    print("1) Fight Monster")
    print("2) Sleep (5 Gold)")
    print("3) Shop")
    print("4) Inventory")
    print("5) Equip Weapon")
    print("6) Save and Quit")
    print("7) Quit Without Saving")
    return get_choice("Choose an option: ", ("1", "2", "3", "4", "5", "6", "7"))


def sleep(state):
    """Restore player health."""
    if state["player_hp"] >= state["max_hp"]:
        print("Your health is already full!")
    elif state["player_gold"] < 5:
        print("You do not have enough gold!")
    else:
        state["player_gold"] -= 5
        state["player_hp"] = state["max_hp"]
        print("You slept and restored your health!")


def make_item(kind):
    """Create an inventory item."""
    if kind == "sword":
        return {
            "name": "Sword",
            "type": "weapon",
            "damage_bonus": 5,
            "maxDurability": 5,
            "currentDurability": 5,
            "equipped": False
        }
    return {
        "name": "Dragon Orb",
        "type": "special",
        "defeats": "Dragon"
    }


def shop(state):
    """Allow the player to purchase items."""
    while True:
        print(f"\nShop - You have {state['player_gold']} gold")
        print("1) Sword (+5 damage, 5 uses) - 20 Gold")
        print("2) Dragon Orb (defeats one Dragon) - 15 Gold")
        print("3) Return to town")

        choice = get_choice("Choose an option: ", ("1", "2", "3"))

        if choice == "3":
            return

        if choice == "1":
            price = 20
            kind = "sword"
        else:
            price = 15
            kind = "orb"

        if state["player_gold"] < price:
            print("You do not have enough gold!")
        else:
            state["player_gold"] -= price
            item = make_item(kind)
            state["player_inventory"].append(item)
            print(f"Purchased {item['name']}! Added to inventory.")


def inventory(state):
    """Display the player's inventory."""
    print("\nYour inventory:")

    if not state["player_inventory"]:
        print("Your inventory is empty.")

    for number, item in enumerate(state["player_inventory"], 1):
        details = " (EQUIPPED)" if item.get("equipped") else ""

        if item["type"] == "weapon":
            details += f" - Durability {item['currentDurability']}/{item['maxDurability']}"

        print(f"{number}) {item['name']} [{item['type']}]{details}")


def equip_weapon(state):
    """Allow the player to equip a weapon."""
    weapons = [
        item for item in state["player_inventory"]
        if item["type"] == "weapon"
    ]

    print("\nChoose a weapon to equip:")
    print("0) None (unequip)")

    for number, item in enumerate(weapons, 1):
        status = " (EQUIPPED)" if item["equipped"] else ""
        print(f"{number}) {item['name']} - {item['currentDurability']} uses left{status}")

    choices = [str(i) for i in range(len(weapons) + 1)]
    choice = get_choice("Choose an option: ", choices)

    for item in weapons:
        item["equipped"] = False

    if choice == "0":
        print("No weapon equipped.")
    else:
        weapon = weapons[int(choice) - 1]
        weapon["equipped"] = True
        print(f"Equipped {weapon['name']}!")


def equipped_weapon(state):
    """Find the equipped weapon."""
    for item in state["player_inventory"]:
        if item["type"] == "weapon" and item.get("equipped"):
            return item
    return None


def attack_monster(state, monster_hp):
    """Attack a monster and reduce weapon durability."""
    damage = 5
    weapon = equipped_weapon(state)

    if weapon:
        damage += weapon["damage_bonus"]
        weapon["currentDurability"] -= 1
        print(f"You attack with your {weapon['name']} for {damage} damage!")

        if weapon["currentDurability"] <= 0:
            state["player_inventory"].remove(weapon)
            print("Your sword broke and was removed from inventory!")
    else:
        print(f"You attack for {damage} damage!")

    return monster_hp - damage


def find_orb(state, monster_name):
    """Find an item that can defeat a monster."""
    for item in state["player_inventory"]:
        if item["type"] == "special" and item["defeats"] == monster_name:
            return item
    return None


def fight_action(state, monster_name):
    """Display available combat actions."""
    print("\n1) Attack")
    print("2) Run away")
    options = ["1", "2"]

    if find_orb(state, monster_name):
        print("3) Use Dragon Orb (instant victory)")
        options.append("3")

    return get_choice("Choose an option: ", options)


def combat_turn(state, monster_name, monster_hp, monster_attack):
    """Perform one combat turn."""
    print(f"\nYour HP: {state['player_hp']}  {monster_name} HP: {monster_hp}")
    action = fight_action(state, monster_name)

    if action == "2":
        print("You ran away!")
        return monster_hp, True

    if action == "3":
        orb = find_orb(state, monster_name)
        state["player_inventory"].remove(orb)
        print(f"Your Dragon Orb defeated the {monster_name} without losing HP!")
        return 0, False

    monster_hp = attack_monster(state, monster_hp)

    if monster_hp > 0:
        state["player_hp"] = max(0, state["player_hp"] - monster_attack)
        print(f"The {monster_name} hits you for {monster_attack} damage!")

    return monster_hp, False


def fight_monster(state):
    """Run combat until victory, defeat, or escape."""
    if state["player_hp"] <= 0:
        print("You have 0 HP. Sleep in town before fighting again!")
        return

    monster_name, monster_hp, monster_attack = random_monster()
    print(f"\nA {monster_name} appeared!")
    escaped = False

    while state["player_hp"] > 0 and monster_hp > 0 and not escaped:
        monster_hp, escaped = combat_turn(
            state, monster_name, monster_hp, monster_attack
        )

    if state["player_hp"] <= 0:
        print("You passed out!")
    elif monster_hp <= 0:
        state["player_gold"] += 3
        print(f"You defeated the {monster_name} and earned 3 gold!")

