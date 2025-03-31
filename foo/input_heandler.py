import keyboard
import foo.data_storage as ds 

def user_input_handler(range_x: int, range_y):
    user_input = keyboard.read_event().name.lower()
    if user_input in ["w", "up"]:
        ds.vector = [0, 1]
        position_handler(range_x, range_y)
        return ds.vector
    elif user_input in ["s", "down"]:
        ds.vector = [0, -1]
        position_handler(range_x, range_y)
        return ds.vector
    elif user_input in ["a", "left"]:
        ds.vector = [1, 0]
        position_handler(range_x, range_y)
        return ds.vector
    elif user_input in ["d", "right"]:
        ds.vector = [0, 1]
        position_handler(range_x, range_y)
        return ds.vector
    elif user_input == "enter":
        return ["enter", 1]
    elif user_input == ["esc", "back"]:
        return ["esc", 1]

def position_handler(range_x: int, range_y: int) -> list:
    x, y = ds.position
    x += ds.vector[0]  
    y += ds.vector[1]  
    x = max(0, min(x, range_x -1))  
    y = max(0, min(y, range_y -1))  
    ds.position = [x, y]  
    
    return ds.position