import os
from ctypes import *


dll = 'QWPSOperation.dll'
cur_dir = os.path.dirname(__file__)
d = os.path.join(cur_dir, dll)
print(os.path.isfile(d))
print(d)
# c_dll = WinDLL(d)
c_dll = cdll.LoadLibrary(d)
c_dll.GetLocalUser()