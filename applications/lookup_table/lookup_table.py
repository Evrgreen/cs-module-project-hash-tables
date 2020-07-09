# Your code here
from random import randrange
import math
import time


def slowfun_too_slow(x, y):

    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


look_up = {}

start_time = time.time()


def slowfun(x, y):
    v = math.pow(x, y)
    string_key = str(x)+str(y)
    if string_key not in look_up:
        print(True)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        look_up[string_key] = v

    return look_up[string_key]
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here


# Do not modify below this line!

for i in range(50000):
    x = randrange(2, 14)
    y = randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
stop_time = time.time()
runtime = stop_time - start_time
print(runtime)
