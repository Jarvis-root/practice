
__all__ = [
    'dabaojian1',
    'dabaojian2'
]


def dabaojian1(money):
    return '至尊享受' if money >= 200 else '基本按摩'


def dabaojian2(money):
    return '双人服务' if money >= 1000 else '单人服务'
