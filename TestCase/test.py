# from .dabaojian import *
import TestCase.dabaojian as a

c = a.dabaojian1
d = a.dabaojian2

def test():
    assert c(200) == '基本按摩'
    assert d(200) == '基本按摩'



