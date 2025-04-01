import foo.data_storage as data
from foo.handlers import menu_handler
from foo.render import render_menu, render_user

# Global dictionary storing functions and their positions




    
def start_game():
    data.vector.clear()
    print("Welcome to Mine Game")
    input("Press Enter to return to main menu...")
    main_menu()  # Return to the main menu after execution

def difficulty():
    data.vector.clear()
    menu_content = {
            "start": "start_game",
            "difficulty": "difficulty",
            "settings": "settings",
            "close": "quit",
    }

    spacing = 15
    name_of_section = "MAIN MENU"
    top_restriction = render_menu(spacing, name_of_section, menu_content)
    menu_handler (menu_content, top_restriction)

def settings():
    data.vector.clear()
    menu_content = {
            "start": "start_game",
            "difficulty": "difficulty",
            "settings": "settings",
            "close": "quit",
    }

    spacing = 15
    name_of_section = "MAIN MENU"
    top_restriction = render_menu(spacing, name_of_section, menu_content)
    menu_handler (menu_content, top_restriction)

def quit():
    data.vector.clear()
    

def main_menu():
    data.menu_position = data.all_menu_functions["main_menu"]
    
    data.vector.clear()
    # initiation of menu API
    menu_content = {
            "start": "start_game",
            "difficulty": "difficulty",
            "settings": "settings",
            "close": "quit",
    }


    spacing = 15
    name_of_section = "MAIN MENU"
    top_restriction = render_menu(spacing, name_of_section, menu_content)
    
    menu_handler (menu_content, top_restriction)

###########################################
# Start the game menu
main_menu()