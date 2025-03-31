import foo.data_storage as ds
# from foo.render import render
from foo import user_input_handler
import time
import os
from foo.render import render_user


def menu():

    menu_content = {"start":[1,1],"difficulty":[1,2],"settings":[1,3],"close":[1,4]}
    # def start_game():
    # def difficulty():
    # def settings():
    # def close
        

    range_x = 15
    menu = "MENU"
    generate_menu = [(menu+" "*(range_x-len(menu))+"|"),("-"*range_x)]
    position_modifier = [range_x,len(generate_menu)]
    for key in menu_content:
        generate_menu.append(f"{key+" " * (range_x- len(key))+"|"}")
    ds.menu_storage =(generate_menu)
    range_y = len(ds.menu_storage)
    while (True):
        print(range_x,range_y)
        print(ds.position)
        print(ds.vector)
        user_input_handler(range_x, range_y )
        os.system('cls' if os.name == 'nt' else 'clear')
        print(render_user(ds.menu_storage.copy(),position_modifier, ds.sprites["menu_cursor"]))
        time.sleep(0.1)
        

menu()