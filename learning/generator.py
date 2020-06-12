def generator():
    for i in range(5):
        yield i


#  这样用永远在第一个元素：  原因： 每次调用generator函数都生成了一个新的<class 'generator'>
print(generator().__next__())
print(generator().__next__())
# print(generator().__next__())
#
# 这样才行，必须保存一个生成器对象，这样就只有一个<class 'generator'> ：
a = generator()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a)
print(type(a))  # <class 'generator'> generator本身是一个function，但是因为yield，他返回的时一个generator类

# 这里是一个简单的例子，演示了生成器和生成器函数的行为:
def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


a = echo(1)
print(next(a))
print(next(a))
print(a.send(2))
a.throw(TypeError, "spam")
a.close()

