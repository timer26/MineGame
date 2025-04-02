# 2D map properties
vector = [0,0]
position_2D = [0, 0]
position_modifier = {
        "x_min": 0,         # left boundary
        "x_max": 0,         # right boundary
        "y_min": 0,         # top boundary
        "y_max": 0,         # bottom boundary
        "x_start": 0,       # force X starting position
        "y_start": 0,       # force Y starting position
}
###########################################

# menu properties data storage
all_menu_functions = {
        "main_menu": [0, 0],
        "start_game": [1, 0],
        "difficulty": [2, 0],
        "settings": [3, 0],
        "quit": [4, 0],
}
menu_position = [0, 0]
last_menu_position = [0, 0]
############################################
# render storage ---> stores API
rendered_area = []
############################################
# all sprite distionary
sprites = {"menu_cursor": " <--"}

def metric_analyse():
     print("vector: ", vector)
     print("position_2D: ", position_2D)
     print("menu_position: ", menu_position)
     print("last_menu_position: ", last_menu_position)