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
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': ['1', 2, '3']
}
user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())
