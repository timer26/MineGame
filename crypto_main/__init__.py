from .menu import (
    main_menu,
    start_game,
    settings,
    end_program
                )
from crypto_main.data_storage import DataStorage
from crypto_main.metric import Metric

metric = Metric(DataStorage())
data = DataStorage(metric)
metric.set_data_storage(data)


__all__ =[
        "data",
        "metric",
        "main_menu",
        "settings",
        "start_game",
        "settings",
        "end_program",
                    ]