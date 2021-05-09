import re

import pytest


def check_ip_re(ip):
    return re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$').match(ip)


def check_ip(ip: str):
    if not isinstance(ip, str):
        return False
    if '.' not in ip:
        return False
    str_list = ip.split('.')
    count = 0
    if len(str_list) == 4:
        for s in str_list:
            if s.isdigit():
                if '0' <= s <= '255':
                    if len(s) > 1:
                        if not s.startswith('0'):
                            count += 1
                    else:
                        count += 1
    return count == 4


@pytest.mark.parametrize('s', [
    '',
    'a',
    '200',
    '256.256.256.256',
    '25,6.25!6.256.25/6',
    '-1.-1.-1.-1',
    '!!!'
])
def test_fail(s):
    assert not check_ip_re(s)
    assert not check_ip(s)


@pytest.mark.parametrize('s', [
    '255.255.255.255',
    '254.254.254.254',
    '0.0.0.0',
    '127.0.0.1',
])
def test_suc(s):
    assert check_ip_re(s)
    assert check_ip(s)


if __name__ == '__main__':
    pytest.main()
