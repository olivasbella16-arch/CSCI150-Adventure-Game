
"""Main program for the text-based adventure game."""

import gamefunctions


def main():
    """Run the town menu until the player chooses to quit."""
    health = 30
    gold = 10

    gamefunctions.print_welcome("Adventurer", 30)

    while True:
        print("\nYou are in town.")
        print("Current HP:", health, "Current Gold:", gold)
        choice = gamefunctions.get_menu_choice()
        if choice == "1":
            health, gold = gamefunctions.fight_monster(health, gold)
        elif choice == "2":
            health, gold = gamefunctions.sleep(health, gold)
        else:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

