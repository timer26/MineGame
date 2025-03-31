import foo.data_storage as ds
# from foo.render import render
from foo import user_input_handler,force_position_handler
import time
import os
from foo.render import render_user


def menu():

    menu_content = {"start":[1,1],"difficulty":[1,2],"settings":[1,3],"close":[1,4]}
    # def start_game():
    # def difficulty():
    # def settings():
    # def close
        

    spaceing = 15
    menu = "MENU"
    generate_menu = [(menu+" "*(spaceing-len(menu))+"|"),("-"*spaceing)]
    top_restriction = len(generate_menu)
    for key in menu_content:
        generate_menu.append(f"{key+" " * (spaceing- len(key))+"|"}")
    ds.menu_storage =(generate_menu)
    range_y = len(ds.menu_storage)
    ds.position_modifier = {
        "x_min": spaceing,                              # Left boundary
        "x_max": spaceing,                              # Right boundary
        "y_min": top_restriction,                       # Top boundary
        "y_max": range_y,                               # Bottom boundary
        "x_start": 0,                                   # force X starting position
        "y_start": 0,                                   # force Y starting position
    }
    force_position_handler([spaceing,top_restriction])
    while (True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(spaceing,range_y," range ")
        print(ds.position, " current position ")
        print(ds.vector," vector ")
        print(render_user(ds.menu_storage.copy(), ds.sprites["menu_cursor"]))
        user_input_handler(spaceing, range_y )
        time.sleep(0.1)
        
menu()