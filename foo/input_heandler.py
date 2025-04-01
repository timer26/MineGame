from pynput import keyboard
import foo.data_storage as ds


def user_input_handler():
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
            ds.vector = [0, -1]
            position_handler()
            return ds.vector
        case "s" | "down":
            ds.vector = [0, 1]
            position_handler()
            return ds.vector
        case "a" | "left":
            ds.vector = [-1, 0]
            position_handler()
            return ds.vector
        case "d" | "right":
            ds.vector = [1, 0]
            position_handler()
            return ds.vector
        case "enter":
            return ["enter", 1]
        case "esc" | "back":
            return ["esc", 1]
        case _:
            return None  # Fallback in case of unexpected input


def position_handler() -> list:
    x, y = ds.position
    dx, dy = ds.vector
    x += dx
    y += dy

    x = max(ds.position_modifier["x_min"], min(x, ds.position_modifier["x_max"]))
    y = max(ds.position_modifier["y_min"], min(y, ds.position_modifier["y_max"] - 1))

    ds.position = [x, y]
    return ds.position


def forced_position_handler(forced_position: list) -> list:
    ds.position = list(forced_position)
    return ds.position