

# 原理：
class MyMeta(type):

    def __new__(mcs, *args, **kwargs):  # 先调用这个 mcs代表metaclass，也就是MyMeta自己
        print(f'mcs: {mcs}')
        print(f'{MyMeta.__name__}, __new__ called!')
        return type.__new__(mcs, *args, **kwargs)  # 返回的是metaclass的实例，也就是类，就是下面的cls

    def __init__(cls, name, bases, attr_dict):  # cls：type.__new__创建的实例，也就是类
        print(f'cls: {cls}')
        print(f'{MyMeta.__name__} ,__init__ called!')
        cls.flag = '使用metaclass把它所有生成的类的属性修改了，牛逼'  # 修改被创建的类的属性
        cls.add_attr = '加一个属性'
        # 以下三种调用方式是等价的：
        # type.__init__(cls, name, bases, attr_dict)
        # super(MyMeta, cls).__init__(name, bases, attr_dict)
        super().__init__(name, bases, attr_dict)

    def __call__(cls, *args, **kwargs):  # call类的实例的时候调用，在metaclass里就是实例化它创建的类是调用
        print(f'cls: {cls}')
        print(f'{MyMeta.__name__} ,__call__ called!)')
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        return obj  # 必须返回一个创建好的对象（实例），不然创建的类实例化的时候就永远是个NoneType


# MyClass = MyMeta('Test', (), {})  # 用MyMeta元类来创建一个Test类
#
# print('-----------------------------------------------')
# print(type(MyClass))
# MyClass()
#
# print('-----------------------------------------------')


class Foo(metaclass=MyMeta):

    flag = 'metaclass可以操作它创建的所有类的属性'
    print(f'原来的：{flag}')

    def __init__(self):  # 如果在metaclass的__call__()中不调用cls.__init__()，连这个方法都不运行
        print('hhhhhhh')
        self.name = 1


f = Foo()
# breakpoint()
print(f'被metaclass修改后的flag：{f.flag}')
print(f'添加的属性：{f.add_attr}')
print(f.name)


"""metaclass有强大的地方，但是也有缺点，太过强大慎用"""
