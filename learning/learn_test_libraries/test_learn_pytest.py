import pytest

import json


# users = json.loads(open('test.json', 'r').read())


# class TestUserPasswordWithParam(object):
#     @pytest.fixture(params=users)
#     def user(self, request):
#         return request.param
#
#     def test_user_password(self, user):
#         passwd = user['password']
#         assert len(passwd) >= 6
#         msg = "user %s has a weak password" %(user['name'])
#         assert passwd != 'password', msg
#         assert passwd != 'password123', msg


@pytest.fixture(scope='module')
def pre(request):
    print(dir(request))
    return 1


@pytest.mark.parametrize('a', [1, 2])
@pytest.mark.usefixtures('pre')
def test_a(a):
    assert a


@pytest.fixture(params=[1, 2, 3, 4, 5])
def multi(request):
    yield request.param


def test_b(multi):
    assert multi > 1


@pytest.mark.parametrize('bb', [1, 2, 3, 4, 5])
def test_c(multi, bb):  # 5 * 5 25次
    assert multi == bb


@pytest.mark.parametrize('c', [1, 2, 3, 4, 5])
def test_d(pre, c):
    assert pre == c
