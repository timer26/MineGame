import time

from modules import render_menu, menu_handler,final_render
from crypto_main.__init__ import data






def run_menu(menu_content: list, spacing: int, name_of_section: str):
    
    render_menu(spacing, name_of_section, menu_content)
    while True:
        final_render(sprite="menu_row_cursor")
        menu_handler(menu_content=menu_content)
# menu functions----------------------------------------------------
def back()->None:
    data.set_menu_position(data.get_last_menu_position())


def difficulty_setter() -> None:
    data.set_menu_position("main_menu")
    pass


# menu pathing -----------------------------------------------------
def start_game()-> None:
    menu_content = [
            "start_game",
            "difficulty",
            "settings",
            "end_game",
    ]

    spacing = 15
    name_of_section = "start_game"
    run_menu(menu_content=menu_content,spacing=spacing,name_of_section= name_of_section)

def difficulty() -> None:
    menu_content = [
            "easy",
            "medium",
            "hard",
            "back"
    ]

    spacing = 15
    name_of_section = "difficulty"
    run_menu(menu_content=menu_content,spacing=spacing,name_of_section= name_of_section)
    
def settings() -> None:
    menu_content = [
            "metrics_analyze",
            "difficulty",
             "back",   
    ]

    spacing = 15
    name_of_section = "settings"
    run_menu(menu_content=menu_content,spacing=spacing,name_of_section= name_of_section)
def end_program()-> None:
    menu_content =["Thanks for playing!"]
    spacing = 15
    name_of_section = "end_game"
    run_menu(menu_content=menu_content,spacing=spacing,name_of_section= name_of_section)
    time.sleep(3)
    exit()


def main_menu():

    #####################---START OF MENU INITIATION---###############
    # initiation of menu API
    menu_content = [
            "start_game",
            "settings",
            "end_game",
    ]

    spacing = 15
    name_of_section = "MAIN MENU"
    run_menu(menu_content=menu_content,spacing=spacing,name_of_section= name_of_section)


data.set_all_menu_functions({
        "main_menu": main_menu,
        "start_game": start_game,
        "difficulty": difficulty,
        "settings": settings,
        "end_game": end_program,
        "back": back,
        "easy": difficulty_setter,
        "medium": difficulty_setter,
        "hard": difficulty_setter,
        # "metrics_analyze"metrics_analyze,
})