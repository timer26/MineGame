from pynput import keyboard
import foo.data_storage as data


from foo import vector, position_2D, menu_position


def metris():
    print(vector)
    print(position_2D)
    print(menu_position)
def user_input_handler()->str:
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
            data.vector = [0, -1]
            position_handler()
            return data.vector
        case "s" | "down":
            data.vector = [0, 1]
            position_handler()
            return data.vector
        case "a" | "left":
            data.vector = [-1, 0]
            position_handler()
            return data.vector
        case "d" | "right":
            data.vector = [1, 0]
            position_handler()
            return data.vector
        case "enter":
            return ["enter", 1]
        case "esc" | "back":
            return ["esc", 1]
        case _:
            return None  # Fallback in case of unexpected input


def position_handler() -> list:
    x, y = data.position_2D
    dx, dy = data.vector
    x += dx
    y += dy

    x = max(data.position_modifier["x_min"], min(x, data.position_modifier["x_max"]))
    y = max(data.position_modifier["y_min"], min(y, data.position_modifier["y_max"] - 1))

    data.position_2D = [x, y]
    return data.position_2D


def forced_position_handler(forced_position: list) -> list:
    data.position_2D = list(forced_position)
    return data.position_2D

def menu_handler(menu_content: dict, top_restriction: int):
    selected_index = data.position_2D[1] - top_restriction  # Convert position to menu index
    menu_keys = list(menu_content.keys())  # Get list of menu keys
    while True:
        print(metris())
        
        result = user_input_handler()
        if result[0] == "enter" or result[0] == "close":
            selected_key = menu_keys[selected_index]
            return menu_content[selected_key]
        
    


