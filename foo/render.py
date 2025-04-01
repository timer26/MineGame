import foo.data_storage as data
from foo import forced_position_handler


def render_user(render_object: list, sprite: str):
        line = render_object[data.position_2D[1]]
        line = list(line)
        line[data.position_2D[0]]= sprite
        render_object[data.position_2D[1]] = ''.join(line)
        return "\n".join(render_object)


def render_menu(spacing: int, name_of_section: str, menu_content: dict)->int:
        """Generates initial menu interface."""
        generate_menu = [(name_of_section + " " * (spacing - len(name_of_section)) + "|"), ("-" * spacing)]
        top_restriction = len(generate_menu)
        # populate menu
        for key in menu_content:
                generate_menu.append(f"{key + ' ' * (spacing - len(key)) + '|'}")
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
        #set accurate position for menu dimension
        forced_position_handler([spacing, top_restriction])
        return top_restriction

def final_render(: