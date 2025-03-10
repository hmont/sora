from typing import Callable

def decorator(**kwargs):
    def wrapper(func: Callable):
        def inner():
            return func(**kwargs)
        return inner
    return wrapper