


class Metric:
    def __init__(self, data_storage):
        self._data_storage = data_storage
        self._metric_data = []


    def _initialize_metrics(self):
        self._metric_data = [
                {"Current vector 2D": self._data_storage.get_vector(), },
                {"Current position 2D": self._data_storage.get_position_2D()},
                {"Minimum X , Y": (self._data_storage.get_position_modifier()["x_min"], self._data_storage.get_position_modifier()["y_min"])},
                {"Maximum X , Y": (self._data_storage.get_position_modifier()["x_max"], self._data_storage.get_position_modifier()["y_max"])},
                {"Forced X , Y":  (self._data_storage.get_position_modifier()["x_start"], self._data_storage.get_position_modifier()["y_start"])},
                {"Current menu": self._data_storage.get_menu_position()},
                {"Previous menu": self._data_storage.get_last_menu_position()},
        ]



    def set_data_storage(self, data_storage):
        self._data_storage = data_storage
        self._initialize_metrics()
        
        
    def set_metric_data(self, value: dict[str, any]) -> None:
        key = list(value.keys())[0]

        # replace if key already exists
        for i, item in enumerate(self._metric_data):
            if key in item:
                self._metric_data[i] = value
                return

        self._metric_data.append(value)

    def get_metric_data(self)->list[dict]:
        return self._metric_data
