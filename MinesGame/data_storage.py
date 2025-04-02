
class DataStorage:
    def __init__(self):
        self._vector = [0, 0]
        self._rendered_area = []
        
        
        self._position_modifier = {
                "x_min": 0,         # left boundary
                "x_max": 0,         # right boundary
                "y_min": 0,         # top boundary
                "y_max": 0,         # bottom boundary
                "x_start": 0,       # force X starting position
                "y_start": 0,       # force Y starting position
                                 }
        self._position_2D = [0, 0]
        
        self._menu_position = [0, 0]
        self._last_menu_position = [0, 0]
        self._all_menu_functions = { 
                "main_menu": [0, 0],
                "start_game": [1, 0],
                "difficulty": [2, 0],
                "settings": [3, 0],
                "quit": [4, 0],
                                    }
        
        
        self._sprites = {
                "menu_cursor": " <--"
        }

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, value):
        self._vector = value

    @property
    def rendered_area(self):
        return self._rendered_area

    @rendered_area.setter
    def rendered_area(self, value):
        self._rendered_area = value

    @property
    def position_modifier(self):
        return self._position_modifier

    @position_modifier.setter
    def position_modifier(self, value):
        self._position_modifier = value

    @property
    def position_2D(self):
        return self._position_2D

    @position_2D.setter
    def position_2D(self, value):
        self._position_2D = value

    @property
    def menu_position(self):
        return self._menu_position

    @menu_position.setter
    def menu_position(self, value):
        self._menu_position = value

    @property
    def last_menu_position(self):
        return self._last_menu_position

    @last_menu_position.setter
    def last_menu_position(self, value):
        self._last_menu_position = value

    @property
    def all_menu_functions(self):
        return self._all_menu_functions

    @all_menu_functions.setter
    def all_menu_functions(self, value):
        self._all_menu_functions = value

    @property
    def sprites(self):
        return self._sprites

    @sprites.setter
    def sprites(self, value):
        self._sprites = value

    def metric_analyse(self):
        return "Metric: Placeholder"  # Stub function

# Singleton instance
data = DataStorage()
