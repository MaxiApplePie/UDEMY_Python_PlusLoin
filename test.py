import sys
import os
import pprint
#
# print(sys.getwindowsversion())
# print(sys.version)
# print(os.__name__)
# print(os.path.dirname.__name__)
#
# print([].extend.__doc__)
#
# print(type(pprint))
# print(type(pprint.pprint))
# print(type(type))
#
# exemple = any([True, False, True])
# print(exemple)
# exemple = all([True, False, True])
# print(exemple)

ages = [15, 16, 17, 18, 19]
print(*ages)
print('*' * 20)
b = [a >= 18 for a in ages]
print(type(b))
print(b)
print(all(a >= 18 for a in ages))
