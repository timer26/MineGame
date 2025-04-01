import foo.data_storage as ds
# from foo.render import render
from foo import user_input_handler,forced_position_handler
import time
import os
from foo.render import render_user


def menu():
    def start_game():
        print("Welcome to Mine Game")
        pass
    def difficulty():
        
        pass
    def settings():
        pass
    def close():
        pass
    menu_content = {"start":start_game(),
                    "difficulty":difficulty(),
                    "settings":settings(),
                    "close":close()
                    }
    print(len(menu_content))
    spaceing = 15
    menu = "MENU"
    generate_menu = [(menu+" "*(spaceing-len(menu))+"|"),("-"*spaceing)]
    top_restriction = len(generate_menu)
#generate initial menu
    for key in menu_content:
        generate_menu.append(f"{key+" " * (spaceing- len(key))+"|"}")
        
    ds.rendered_area =(generate_menu)
    range_y = len(ds.rendered_area)
    ds.position_modifier = {
        "x_min": spaceing,                              # Left boundary
        "x_max": spaceing,                              # Right boundary
        "y_min": top_restriction,                       # Top boundary
        "y_max": range_y,                               # Bottom boundary
        "x_start": spaceing,                            # force X starting position
        "y_start": top_restriction,                     # force Y starting position
    }
    forced_position_handler([spaceing,top_restriction])
    menu_option = list(menu_content.items())
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(spaceing,range_y," range ")
        print(ds.position, " current position ")
        print(ds.vector, " vector ")
        print(render_user(ds.rendered_area.copy(), ds.sprites["menu_cursor"]))
        result = user_input_handler()
       
        print("-------------------------------")
            
menu()