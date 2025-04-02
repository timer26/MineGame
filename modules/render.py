from MinesGame.data_storage import data
from modules.handlers import forced_position_handler, user_input_handler
import os
def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

def render_menu(spacing: int, name_of_section: str, menu_content: list) -> int:
        # generates initial menu interface
        generate_menu = [(name_of_section + " " * (spacing - len(name_of_section)) + "|"), ("-" * spacing)]
        top_restriction = len(generate_menu)

        # Populate menu
        for value in menu_content:
                generate_menu.append(f"{value + ' ' * (spacing - len(value)) + '|'}")

        data.rendered_area = generate_menu
        range_y = len(data.rendered_area)

        data.position_modifier = {
                "x_min": spacing,
                "x_max": spacing,
                "y_min": top_restriction,
                "y_max": range_y,
                "x_start": spacing,
                "y_start": top_restriction,
        }

        # Set accurate position for menu dimension
        forced_position_handler([spacing, top_restriction])

def render_user(render_object: list, sprite: str):
        line = render_object[data.position_2D[1]]
        line = list(line)
        line[data.position_2D[0]]= sprite
        render_object[data.position_2D[1]] = ''.join(line)
        return "\n".join(render_object)


def final_render(sprite: str):
        clear_console()
        print(data.metric_analyse())
        print(render_user(data.rendered_area.copy(), data.sprites[sprite]))
