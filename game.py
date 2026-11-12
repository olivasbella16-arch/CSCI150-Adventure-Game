

"""Main entry point for the text-based adventure game."""

import gamefunctions


def main():
    """Initialize game state and run the town menu until quitting."""
    state = {
        "player_name": "Adventurer",
        "player_hp": 30,
        "max_hp": 30,
        "player_gold": 100,
        "player_inventory": []
    }

    gamefunctions.print_welcome(state["player_name"], 30)

    actions = {
        "1": gamefunctions.fight_monster,
        "2": gamefunctions.sleep,
        "3": gamefunctions.shop,
        "4": gamefunctions.inventory,
        "5": gamefunctions.equip_weapon
    }

    while True:
        choice = gamefunctions.town_menu(state)
        if choice == "6":
            print("Thanks for playing!")
            break
        actions[choice](state)


if __name__ == "__main__":
    main()
