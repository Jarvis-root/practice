import time, random
"""
装饰器学习
闭包函数：闭包函数必须满足两个条件:1.函数内部定义的函数 2.包含对外部作用域而非全局作用域的引用
装饰器：外部函数传入被装饰函数名，内部函数返回装饰函数名
"""

# x = 1
# def funx():
#     "非闭包"
#     def func1():
#         print(x)
#     func1()
#
# funx()
# print(x)  # 打印出1
#
#
# def outer():
#     """闭包"""
#     x = 1
#     y = 2
#
#     def inner():
#         print("x= %s" %x)
#         print("y= %s" %y)
#
#     print(inner.__closure__)
#     return inner
#
# outer()


# from urllib.request import urlopen
#
# def index(url):
#     """闭包"""
#     def get():
#         with open("test.html", 'w') as f:
#             f.write(urlopen(url).read().decode())
#         return f
#     return get
#
# python = index("http://www.python.org") # 返回的是get函数的地址
# print(python()) # 执行get函数《并且将返回的结果打印出来



"""这是一个无参装饰器例子"""
# def outer1(func):  # 将index的地址传递给func
#     def inner():
#         start_time = time.time()
#         func()   # fun = index  即func保存了外部index函数的地址
#         end_time = time.time()
#         print("运行时间为%s"%(end_time - start_time))
#     return inner  # 返回inner的地址
#
#
# def index():
#     time.sleep(random.randrange(1, 5))
#     print("welcome to index page")
#
# index = outer1(index)  # 这里返回的是inner的地址，并重新赋值给index
# index()

#上面也可以写成：
# @outer1
# def index():
#     time.sleep(random.randrange(1, 5))
#     print("welcome to index page")
# index()

# """下面是带参数的装饰砌，切被装饰函数有返回值"""
# def outer1(func):  # 将index的地址传递给func
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         ret = func(*args, **kwargs)
#         end_time = time.time()
#         print("运行时间为%s"%(end_time - start_time))
#         return ret
#     return inner  # 返回inner的地址
#
#
# @outer1
# def index(limit):
#     time.sleep(random.randrange(1, limit))
#     print("welcome to index page")
#     return "随便返回点什么"
#
# print(index(3))


"""类装饰器写法一"""
class Foo(object):

    def __call__(self, func):
        def _call(*args, **kw):
            print('class decorator runing')
            return func(*args, **kw)

        return _call


@Foo()
def bar(test, ids):   # bar = Foo()(bar)
    print(test, ids)


bar('aa', 555)


"""类装饰器写法2"""
class Foo1(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kw):
        print('class decorator runing')
        return self.func(*args, **kw)


@Foo1
def bar(test, ids):
    print(test, ids)


bar('aa', 555)
