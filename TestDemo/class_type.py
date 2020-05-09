"""
Python是动态语言，Python中的对象可以动态地创建，我们可以给对象动态地添加删除属性，方法等。
那么类既然是对象，按理说也是可以动态地创建。
其实在python中，我们使用class创建类，当你使用class关键字时，Python解释器自动创建这个对象。
而底层其实使用的是type函数(type函数也可以查看实例所属类型)来创建类的。所以我们可以直接使用type()函数来手动实现动态创建类。"""


class Person(object):
    print("不调用类，也会执行我")

    def __init__(self, name):
        self.name = name

    def p(self):
        print("this is a  methond")


print(Person)
tom = Person("tom")
print("tom实例的类型是：%s" % type(tom))  # 实例tom是Person类的对象。
print("Peron类的类型：%s" % type(Person))  # 结果看出我们创建的类属于type类,也就是说Person是type类的对象
print("type的类型是：%s" % type(type))

print('元类就是类的类，python中函数type实际上是一个元类。type就是Python在背后用来创建所有类的元类-')
# 1.自动使用class关键字创建一个类
class Student1(object):
    pass

# 2.使用type函数手动创建一个类
Student2 = type("Student2", (), {})

s1 = Student1()  # 同样都可以创建实例
s2 = Student2()  # 同样都可以创建实例

print(type(Student1), type(Student2))
print(type(s1), type(s2))

# 使用type创建带有属性的类, 添加的属性是类属性，并不是实例属性
Girl = type("Girl", (), {"country": "china", "sex": "male"})
girl = Girl()
print(girl.country, girl.sex)  # 使用type创建的类，调用属性时IDE不会自动提示补全
print(type(girl), type(Girl))



print("python中方法有普通方法，类方法，静态方法")
# 使用type创建带有方法的类
def speak(self):
    print("这是给类添加的普通方法")


@classmethod
def c_run(cls):
    print("这是给类添加的类方法")


@staticmethod
def s_eat():
    print("这是给类添加的静态方法")


# 创建类，给类添加静态方法，类方法，普通方法。跟添加类属性差不多.
Boy = type("Boy", (), {"speak": speak, "c_run": c_run, "s_eat": s_eat, "sex": "female"})
boy = Boy()
boy.speak()
boy.s_eat()  # 调用类中的静态方法
boy.c_run()  # 调用类中类方法
print("boy.sex:", boy.sex)
print(type(boy), type(Boy))
