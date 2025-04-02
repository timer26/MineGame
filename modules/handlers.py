from modules import *

from pynput import keyboard

def user_input_handler() -> str:
    pressed_key = []

    def on_press(key):
        try:
            k = key.char.lower()
        except AttributeError:
            k = key.name  # Handle special keys like "enter", "esc", etc.

        valid_keys = {"w", "a", "s", "d", "up", "down", "left", "right", "enter", "esc", "back"}
        if k in valid_keys:
            pressed_key.append(k)
            return False  # Stop the listener

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    user_input = pressed_key[0]

    match user_input:
        case "w" | "up":
            data.set_vector([0, -1])
            position_handler()
            return data.get_vector()
        case "s" | "down":
            data.set_vector([0, 1])
            position_handler()
            return data.get_vector()
        case "a" | "left":
            data.set_vector([-1, 0])
            position_handler()
            return data.get_vector()
        case "d" | "right":
            data.set_vector([1, 0])
            position_handler()
            return data.get_vector()
        case "enter":
            return ["enter", 1]
        case "esc":
            return ["esc", -1]
        case "back":
            return ["back", -1]
        case _:
            return None  # Fallback in case of unexpected input

def position_handler() -> list:
    x, y = data.get_position_2D()
    dx, dy = data.get_vector()
    x += dx
    y += dy

    modifier = data.get_position_modifier()
    x = max(modifier["x_min"], min(x, modifier["x_max"]))
    y = max(modifier["y_min"], min(y, modifier["y_max"] - 1))

    data.set_position_2D([x, y])
    return data.get_position_2D()

def forced_position_handler(forced_position: list) -> list:
    data.set_position_2D(list(forced_position))
    return data.get_position_2D()

def menu_handler(menu_content: list):
    position = data.get_position_2D()
    modifier = data.get_position_modifier()
    selected_index = position[1] - modifier["y_start"]  # Convert position to menu index

    result = user_input_handler()
    if result[0] == "enter":
        data.set_last_menu_position(data.get_menu_position().copy())
        selected_key = menu_content[selected_index]
        data.set_menu_position(data.get_all_menu_functions()[selected_key])

    elif result[0] in ["esc", "back"]:
        menu_position = data.get_menu_position()
        if result[0] == "esc":
            menu_position = [0, 0]
        else:
            menu_position[1] = max(0, menu_position[1] + result[1])
        data.set_menu_position(menu_position)
        data.set_last_menu_position(menu_position.copy())

    return menu_content[selected_index]