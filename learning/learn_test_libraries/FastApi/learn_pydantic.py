from datetime import datetime
from itertools import permutations
from typing import List
from pydantic import BaseModel

"""
pydantic:
Data validation and settings management using python type annotations.
pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
Define how data should be in pure, canonical python; validate it with pydantic.
pydantic使用python的类型注解来校验数据
"""


class User(BaseModel):
    id: int
    name = 1  # 如果没有写类型注解，就按变量的值确定类型
    signup_ts: datetime
    friends: List[int]


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': ['1', 2, '3'],
    'name': 'liudong'
}
# 如果传递的数据不符合类型提示，或者不能转化为提示的类型，pydantic会报validation error
user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())
