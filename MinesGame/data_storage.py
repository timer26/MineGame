from MinesGame.menu import *
class DataStorage:
    def __init__(self):
        self._vector = [0, 0]
        self._position_2D = [0, 0]
        self._rendered_area = []
        
        
        self._position_modifier = {
                "x_min": 0,         # left boundary
                "x_max": 0,         # right boundary
                "y_min": 0,         # top boundary
                "y_max": 0,         # bottom boundary
                "x_start": 0,       # force X starting position
                "y_start": 0,       # force Y starting position
                                 }
        
   
              
        self._menu_position = ""
        self._last_menu_position: list[str] = []
        self._all_menu_functions = {}
        
        
        self._sprites = {
                "menu_cursor": " <--"
        }



        self._metric_data =   [
                {"Current vector 2D": self._vector},
                {"Current position 2D": self._position_2D},
                {"Maximum X , Y": (self._position_modifier["x_max"], self._position_modifier["y_max"])},
                {"Minimum X , Y": (self._position_modifier["x_min"], self._position_modifier["y_min"])},
                {"Forced X , Y":  (self._position_modifier["x_start"], self._position_modifier["y_start"])},
        ]

    





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

    def get_last_menu_position(self) -> str:
        if self._last_menu_position:
            return self._last_menu_position.pop()
        return "main_menu"  # fallback if empty


    def get_all_menu_functions(self):
        return self._all_menu_functions

    def get_sprites(self)->str:
        return self._sprites
    def get_metric_data(self)->list[dict]:
        return self._metric_data
    
    #########- setters -##############
    def set_vector(self, value: list[int,int]) -> None:
        self._vector = value

    def set_rendered_area(self, value: list[str]) -> None:
        self._rendered_area = value

    def set_position_modifier(self, value: dict[str, int]) -> None:
        self._position_modifier = value

    def set_position_2D(self, value: list[int,int]) -> None:
        self._position_2D = value

    def set_menu_position(self, value:str) -> None:
        self._menu_position = value

    def set_last_menu_position(self, value: str) -> None:
        self._last_menu_position.append(value)

    def set_all_menu_functions(self, value: dict[str, callable]) -> None:
        self._all_menu_functions = value

    def set_metric_data(self, value: dict[str, any]) -> None:
        self._metric_data.append(value)
        
data = DataStorage()
