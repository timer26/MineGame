import keyboard
import foo.data_storage as ds 

def user_input_handler():
    user_input = keyboard.read_event().name.lower()
    if user_input in ["w", "up"]:
        ds.vector = [0, -1]
        position_handler()
        return ds.vector
    elif user_input in ["s", "down"]:
        ds.vector = [0, 1]
        position_handler()
        return ds.vector
    elif user_input in ["a", "left"]:
        ds.vector = [-1, 0]
        position_handler()
        return ds.vector
    elif user_input in ["d", "right"]:
        ds.vector = [1, 0]
        position_handler()
        return ds.vector
    elif user_input == "enter":
        return ["enter", 1]
    elif user_input == ["esc", "back"]:
        return ["esc", 1]

def position_handler() -> list:

    x, y = ds.position
    x += ds.vector[0]  
    y += ds.vector[1]
    x = max(ds.position_modifier["x_min"], min(x, ds.position_modifier["x_max"]))
    y = max(ds.position_modifier["y_min"], min(y, ds.position_modifier["y_max"]))

    ds.position = [x, y]  
    
    return ds.position

def forced_position_handler(forced_position:list) -> list:
    ds.position = forced_position[0], forced_position[1]