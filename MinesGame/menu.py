from modules import data, render_menu, menu_handler,final_render
# Global dictionary storing functions and their positions





def start_game():
    print("Welcome to Mine Game!")
    data.vector.clear()
    pass

def difficulty():
    print("deffulty")
    data.vector.clear()
    pass

def settings():
    print("settings")
    data.vector.clear()
    pass
def end_game():
    exit()


def main_menu():

    #####################---START OF MENU INITIATION---###############
    # initiation of menu API
    menu_content = [
            "start_game",
            "difficulty",
            "settings",
            "quit",
    ]

    spacing = 15
    name_of_section = "MAIN MENU"
    render_menu(spacing, name_of_section, menu_content)
    #####################---END OF MENU INITIATION---###############

    ########################---CODE SEGMENT---######################

    ###############################################################
    while True:
        final_render("menu_cursor")
        menu_handler(menu_content)


###########################################
# Start the game menu