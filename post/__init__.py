import functools
import time
import threading


def deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()

    return wrapper


@deco
def foo(x, y):
    c = 0
    while c < 5:
        c = c + 1
        print('x: {}, y: {}'.format(x, y))
        time.sleep(1)


foo(123, 456)