from __future__ import annotations

# 内置的 breakpoint()


breakpoint()

# PEP 563：延迟的标注求值
# 标注只能使用在当前作用域中已经存在的名称，也就是说，它们不支持任何形式的前向引用；而且——
# 标注源码对 Python 程序的启动时间有不利的影响。
class C:
    @classmethod
    def from_string(cls, source: str) -> C:
        pass

    def validate_b(self, obj: B) -> bool:
        pass

    def __await__(self):
        pass


class B:
    pass

# 定制对模块属性的访问
# 允许在模块上定义 __getattr__() 并且当以其他方式找不到某个模块属性时将会调用它。 在模块上定义 __dir__() 现在也是允许的。
def __dir__():
    return ''


def __getattr__(name):
    if name == 'C':
        return C


# async 和 await 现在是保留的关键字
async def demo():
    await C()


# 新的 dataclass() 装饰器提供了一种声明 数据类 的方式。 数据类使用变量标注来描述其属性。
# 它的构造器和其他魔术方法例如 __repr__(), __eq__() 以及 __hash__() 会自动地生成。
from dataclasses import dataclass

@dataclass
class Point(object):
    x: float
    y: float
    z: float = 0.0

p = Point(1.5, 2.5)
print(p)   # produces "Point(x=1.5, y=2.5, z=0.0)"

print(Point)