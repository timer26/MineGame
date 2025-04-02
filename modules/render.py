from modules import forced_position_handler
from MinesGame.data_storage import data
import os

def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

def render_menu(spacing: int, name_of_section: str, menu_content: list):
        generate_menu = [(name_of_section + " " * (spacing - len(name_of_section)) + "|"), ("-" * spacing)]
        top_restriction = len(generate_menu)

        for value in menu_content:
                generate_menu.append(f"{value + ' ' * (spacing - len(value)) + '|'}")

        data.set_rendered_area(generate_menu)
        range_y = len(data.get_rendered_area())

        data.set_position_modifier({
                "x_min": spacing,
                "x_max": spacing,
                "y_min": top_restriction,
                "y_max": range_y,
                "x_start": spacing,
                "y_start": top_restriction,
        })

        forced_position_handler([spacing, top_restriction])

def render_user(render_object: list, sprite: str):
        position_2D = data.get_position_2D()
        line = render_object[position_2D[1]]
        line = list(line)
        line[position_2D[0]] = sprite
        render_object[position_2D[1]] = ''.join(line)
        return "\n".join(render_object)

def render_matric():

        data.get_vector()       


def final_render(sprite: str):
        clear_console()
        print(data.get_menu_position())
        print(data.get_last_menu_position())
        print(render_user(data.get_rendered_area().copy(), data.get_sprites()[sprite]))
