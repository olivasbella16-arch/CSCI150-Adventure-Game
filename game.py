
"""Main program for the adventure game with JSON saving and loading."""

import json
import os
import gamefunctions


SAVE_FILE = "game_save.json"


def create_new_game():
    """Create a new player's starting game state."""
    name = input("What is your name? ").strip()

    if not name:
        name = "Adventurer"

    return {
        "player_name": name,
        "player_hp": 30,
        "max_hp": 30,
        "player_gold": 100,
        "player_inventory": []
    }


def save_game(state):
    """Save the complete player state to a JSON file."""
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as save_file:
            json.dump(state, save_file, indent=4)

        print(f"Game saved successfully to {SAVE_FILE}!")
        return True

    except OSError as error:
        print(f"Error saving game: {error}")
        return False


def load_game():
    """Load the player's saved state from a JSON file."""
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as save_file:
            state = json.load(save_file)

        required_keys = [
            "player_name",
            "player_hp",
            "max_hp",
            "player_gold",
            "player_inventory"
        ]

        if not all(key in state for key in required_keys):
            print("Save file is missing required information.")
            return None

        if not isinstance(state["player_inventory"], list):
            print("Saved inventory is invalid.")
            return None

        print(f"Welcome back, {state['player_name']}!")
        print("Your saved game has been loaded!")
        return state

    except FileNotFoundError:
        print("No saved game was found.")
        return None

    except (json.JSONDecodeError, OSError, TypeError):
        print("Could not read the saved game.")
        return None


def start_menu():
    """Allow the player to start a new game or load a saved game."""
    while True:
        print("\nWELCOME TO THE ADVENTURE GAME!")
        print("1) Start a New Game")
        print("2) Load Saved Game")
        print("3) Quit")

        choice = gamefunctions.get_choice(
            "Choose an option: ", ("1", "2", "3")
        )

        if choice == "1":
            return create_new_game()

        elif choice == "2":
            state = load_game()

            if state is not None:
                return state

        else:
            return None


def main():
    """Run the main game loop."""
    state = start_menu()

    if state is None:
        print("Thanks for playing!")
        return

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
            if save_game(state):
                print("Your game has been saved. See you next time!")
                break

        elif choice == "7":
            print("You quit without saving. Thanks for playing!")
            break

        else:
            actions[choice](state)


if __name__ == "__main__":
    main()
