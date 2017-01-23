from katakana import *
from hiragana import *
from slogi import *
def add_2(x, y):
    k=list(map(lambda a, b: a + b, x, y))
    return k
def add_3(x, y, z):
    k=list(map(lambda a, b, c: a+b+c, x, y, z))
    return k