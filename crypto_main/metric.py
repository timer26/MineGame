from crypto_main.data_storage import data


class Metric:
    def __init__(self, data):

        self._metric_data = [
                {"Current vector 2D": data.get_vector(),},
                {"Current position 2D": data.get_position_2D()},
                {"Minimum X , Y": (data.get_position_modifier()["x_min"], data.get_position_modifier()["y_min"])},
                {"Maximum X , Y": (data.get_position_modifier()["x_max"], data.get_position_modifier()["y_max"])},
                {"Forced X , Y":  (data.get_position_modifier()["x_start"], data.get_position_modifier()["y_start"])},
                {"Current menu": data.get_menu_position()},
                {"Previous menu": data.get_last_menu_position()},
        ]


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

metric = Metric(data)