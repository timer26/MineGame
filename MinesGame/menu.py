import time

from modules import render_menu, menu_handler,final_render
from MinesGame.data_storage import data
# Global dictionary storing functions and their positions






def run_menu(menu_content: list, spacing: int, name_of_section: str):
    
    render_menu(spacing, name_of_section, menu_content)
    while True:
        final_render("menu_cursor")
        print(menu_handler(menu_content))

def back():
    if data.get_last_menu_position() != (None, "main_menu"):
        last_menu_key = data.get_last_menu_position()
        data.set_menu_position(last_menu_key)
        data.get_all_menu_functions()[last_menu_key]()
    
def start_game():
    menu_content = [
            "start_game",
            "difficulty",
            "settings",
            "end_game",
    ]

    spacing = 15
    name_of_section = "start_game"
    run_menu(menu_content, spacing, name_of_section)

def difficulty():
    menu_content = [
            "start_game",
            "difficulty",
            "settings",
            "end_game",
            "back"
    ]

    spacing = 15
    name_of_section = "difficulty"
    run_menu(menu_content, spacing, name_of_section)
def settings():
    menu_content = [
            "metrics_analyze",
            # "size_of_game",   
    ]

    spacing = 15
    name_of_section = "settings"
    run_menu(menu_content, spacing, name_of_section)
def end_game():
    menu_content =["Thanks for playing!"]
    spacing = 15
    name_of_section = "end_game"
    render_menu(spacing, name_of_section, menu_content)
    time.sleep(3)
    exit()


def main_menu():

    #####################---START OF MENU INITIATION---###############
    # initiation of menu API
    menu_content = [
            "start_game",
            "difficulty",
            "settings",
            "end_game",
    ]

    spacing = 15
    name_of_section = "MAIN MENU"
    run_menu(menu_content, spacing, name_of_section)


data.set_all_menu_functions({
        "main_menu": main_menu,
        "start_game": start_game,
        "difficulty": difficulty,
        "settings": settings,
        "end_game": end_game,
        "back": back
})