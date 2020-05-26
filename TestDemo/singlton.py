# 装饰器实现单例
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


@singleton
class Cls(object):
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))


# new方法
class Single(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


single1 = Single()
single2 = Single()
print(id(single1) == id(single2))


# 使用metaclass
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cls4(metaclass=Singleton):
    pass


cls1 = Cls4()
cls2 = Cls4()
print(id(cls1) == id(cls2))

