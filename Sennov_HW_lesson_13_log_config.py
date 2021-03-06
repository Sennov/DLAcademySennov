"""
Реализовать логгирование для вашего чата (из предыдущего дз) с использованием модуля logging:
1. Реализовать декоратор @log, фиксирующий обращение к декорируемой функции:
сохраняет имя функции и её аргументы.
2. Настройку логгера выполнить в отдельном модуле log_config.py:
Создание именованного логгера.;
Сообщения лога должны иметь следующий формат: "<дата-время> <уровень_важности> <имя_модуля> <имя_функции> 
<сообщение>"
Пример того, как это должно выглядеть указан на следующем слайде
"""
import logging

logging.basicConfig(
    filename = 'hw13_app.log',
    format = "%(name)-5s %(asctime)s %(levelname)-8s %(filename)-15s %(funcName)-10s %(message)s",
    level = logging.INFO
    )

log = logging.getLogger('logg')

