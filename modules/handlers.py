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
    
    data.set_metric_data({"Latest key pressed": pressed_key})   #sending data to metric storage
    
    if user_input in ("w", "up"):
        data.set_vector([0, -1])
        position_handler()
        return data.get_vector()
    elif user_input in ("s", "down"):
        data.set_vector([0, 1])
        position_handler()
        return data.get_vector()
    elif user_input in ("a", "left"):
        data.set_vector([-1, 0])
        position_handler()
        return data.get_vector()
    elif user_input in ("d", "right"):
        data.set_vector([1, 0])
        position_handler()
        return data.get_vector()
    elif user_input == "enter":
        return "enter"
    elif user_input == "esc":
        return "esc"
    elif user_input == "back":
        return "backspace"
    else:
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

    # Metric logging
    data.set_metric_data({"Last menu position": data.peek_last_menu_position()})
    data.set_metric_data({"Current menu position": data.get_menu_position()})

    if result == "enter":
        data.set_last_menu_position(data.get_menu_position())
        data.set_menu_position(selected_key)
        data.get_all_menu_functions()[selected_key]()

    elif result == "esc":
        data.set_menu_position("main_menu")
        data.get_all_menu_functions()["main_menu"]()

    elif result == "backspace":
        data.get_all_menu_functions()["back"]()

    return selected_key