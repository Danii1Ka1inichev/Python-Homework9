from datetime import datetime
import logging

def decorator2(function):
    def wrapper(x, y):
        logging.basicConfig(
            level=logging.DEBUG,
            filename="mylog.log",
            format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
            datefmt='%H:%M:%S',
        )
        logging.info(f'Входные значения x:{x}, y:{y}')
        start_time = datetime.now()
        sum = function(x, y)
        logging.info(f'Результат работы функции:{sum}')
    return wrapper


@decorator2
def function(x, y):
    sum = x**y**y
    return sum


decorator2(function(5, 5))