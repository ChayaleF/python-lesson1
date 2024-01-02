import sys
from functools import lru_cache
import datetime
import time

def timein(func):
    def inner():
        timestart=time.time()
        func()
        print(time.time()-timestart)
    return inner()

def print_hi(name):
    print(f'Hi, {name}')

@timein
def formil():
    for i in range(1000000):
        print(i)


@lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

print([fibonacci(x) for x in range(1222)])
def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
