import foo.data_storage as data

def render_user(render_object: list, sprite: str):
        line = render_object[data.position[1]]
        line = list(line)
        line[data.position[0]]= sprite
        render_object[data.position[1]] = ''.join(line)
        return "\n".join(render_object)