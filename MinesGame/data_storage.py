
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



##########- getters -################
    def get_vector(self):
        return self._vector
    
    def get_rendered_area(self):
        return self._rendered_area
    
    def get_position_modifier(self):
        return self._position_modifier
    
    def get_position_2D(self):
        return self._position_2D
    
    def get_menu_position(self):
        return self._menu_position
    
    def get_last_menu_position(self):
        return self._last_menu_position

    def get_all_menu_functions(self):
        return self._all_menu_functions

    def get_sprites(self):
        return self._sprites
    #########- setters -##############
    def set_vector(self, value):
        self._vector = value
        
    def set_rendered_area(self, value):
        self._rendered_area = value

    def set_position_modifier(self, value):
        self._position_modifier = value

    def set_position_2D(self, value):
        self._position_2D = value

    def set_menu_position(self, value):
        self._menu_position = value

    def set_last_menu_position(self, value):
        self._last_menu_position = value

    def set_all_menu_functions(self, value):
        self._all_menu_functions = value

    def set_sprites(self, value):
        self._sprites = value

    def metric_analyse(self):
        return "Metric: Placeholder"  # Stub function

# Singleton instance
data = DataStorage()
