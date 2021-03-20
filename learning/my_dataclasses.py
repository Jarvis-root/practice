import dataclasses


@dataclasses.dataclass(frozen=True)
class SomeData(object):
    name: str
    habit: str


@dataclasses.dataclass(frozen=True)
class SomeData2(object):
    name: str = 'jack'
    habit: str = 'sleep'


if __name__ == '__main__':
    # print(SomeData.__annotations__)
    # print(dir(SomeData))
    # print(SomeData.__dict__)
    # print(SomeData.__doc__)

    SomeData2.name = 'mark'
    print(SomeData2.name)
    print(SomeData2.habit)

    # 自动生成__init__, frozen为True的话在实例化后值不准变化
    data = SomeData(name='sada', habit='eat')
    print(data.name)
    # data.habit = '111'  # dataclasses.FrozenInstanceError
