
import keyboard

picus

# general 0 = string handling / 1 = int handling
def user_input_handler(general: int):

    def strings() -> str:
        while True:
            user_input = keyboard.read_event().name.lower()
            if user_input in ["w", "up"]:
                return "up"
            elif user_input in ["s", "down"]:
                return "down"
            elif user_input in ["a", "left"]:
                return "left"
            elif user_input in ["d", "right"]:
                return "right"
            elif user_input == "enter":
                return  "enter"
            elif user_input == ["esc", "back"]:
                return  "esc"

    def numbers():
            pass


    if general == 0 :
        strings()
    elif general == 1:
        numbers()

def menu():
    current_position = 0  # Store menu position globally within menu()

    def current_position_in_menu(position: int):
        nonlocal current_position  # Allows modification of outer function variable
        current_position = position
        return current_position

    def display_settings():
        current_position_in_menu(1)
        print("Display settings - Position:", current_position)

    def difficulty():
        current_position_in_menu(2)
        print("Difficulty - Position:", current_position)

    def start_game():
        current_position_in_menu(3)
        print("Game start - Position:", current_position)

    def close():
        current_position_in_menu(4)
        print("Closing - Position:", current_position)

    # Dictionary for menu
    main_menu = {
        "display setting": "display_settings",
        "difficulty": "difficulty",
        "start game": "start_game",
        "close": "close"
    }


    while True:

        len(main_menu)

        print("MENU")
        print(""*20)
        for key in main_menu:
            spacing = 20 - len(key)
            print(key," "* spacing,"|")


# Call menu
menu()