import foo.data_storage as ds

def render_user(render_object: list, sprite: str):
        line = render_object[ds.position[1]]
        line = list(line)
        line[ds.position[0]]= sprite
        render_object[ds.position[1]] = ''.join(line)
        return "\n".join(render_object)