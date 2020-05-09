

class A(object):
    def __new__(cls, *args, **kwargs):
        print('__new__ called')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('__init__ called')

a = A()
print(id(a))

class B(object):
    def __new__(cls, *args, **kwargs):
        print('__new__ called')
        return 1

    def __init__(self):
        print('__init__ called')

b = B()
print(type(b))
print(id(b))