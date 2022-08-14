from datetime import datetime

def decorator3(function):
    def wrapper(x, y):
        start_time = datetime.now()
        sum = function(x, y)
        print(sum)
        print(f'Время выполнение функции: {datetime.now() - start_time}')
    return wrapper


@decorator3
def function(x, y):
    return x**y**y


decorator3(function(5, 5))