import time

from modules import *
from MinesGame.data_storage import data
from pynput import keyboard

def user_input_handler() -> str:
    pressed_key = []

    def on_press(key):
        try:
            k = key.char.lower()
        except AttributeError:
            k = key.name  # Handle special keys like "enter", "esc", etc.

        valid_keys = {"w", "a", "s", "d", "up", "down", "left", "right", "enter", "esc", "backspace"}
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
            return ["backspace", -1]
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
    data.set_vector([0, 0])
    selected_option = data.get_position_2D()[1] - data.get_position_modifier()["y_start"]
    result = user_input_handler()

    selected_key = menu_content[selected_option]

    if result[0] == "enter":
        data.set_last_menu_position(data.get_menu_position()) 
        data.set_menu_position(selected_key)
        data.get_all_menu_functions()[selected_key]()

    elif result[0] == "esc":
        data.set_menu_position("main_menu")
        data.get_all_menu_functions()["main_menu"]()

    elif result[0] == "backspace":
        data.get_all_menu_functions()["back"]()

    return selected_key
