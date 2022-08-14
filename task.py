cache = dict()
list_of_cache = []


def decorator1(function):
    def wrapper(x, y):
        intro = f'{x}, {y}'
        if intro not in cache:
            cache[intro] = function(x, y)
            if len(list_of_cache) >= 3:
                cache.pop(list_of_cache[0])
                list_of_cache.__delitem__(0)
            list_of_cache.append(intro)
            sum = cache[intro]
            return sum

        else:
            sum = cache[intro]
            return sum

    return wrapper


@decorator1
def function(x, y):
    return x**y


decorator1(function(5, 5))
decorator1(function(25, 5))
decorator1(function(7, 5))
print(cache)
print(list_of_cache)
decorator1(function(8, 5))

print(cache)
print(list_of_cache)

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
