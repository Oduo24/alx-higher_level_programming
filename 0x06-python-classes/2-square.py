#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        self.set_size(size)

    def set_size(self, size):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


mysquare1 = Square(3)
print(type(mysquare1))
print(mysquare1.__dict__)

mysquare2 = Square()
print(type(mysquare2))
print(mysquare2.__dict__)

try:
    print(mysquare1.size)
except Exception as e:
    print(e)

try:
    print(mysquare1.__size)
except Exception as e:
    print(e)

try:
    mysquare3 = Square("3")
    print(type(mysquare3))
    print(mysquare3.__dict__)
except Exception as e:
    print(e)

try:
    mysquare4 = Square(-89)
    print(type(mysquare4))
    print(mysquare4.__dict__)
except Exception as e:
    print(e)
