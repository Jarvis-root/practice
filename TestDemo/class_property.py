class Goods(object):
    name: str = 4164161
    price: float


# 类属性与实例属性不相互独立
if __name__ == '__main__':
    print(Goods.name)
    Goods.name = "sdasda"
    print(Goods.name)

    g1 = Goods()
    g1.name = 'a'
    g2 = Goods()
    g2.name = 'b'
    print(g1.name)
    print(g2.name)
    print(Goods.name)