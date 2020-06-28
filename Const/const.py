import sys



class const:
    class ConstError(TypeError):
        pass


    def __setattr__(cls, key, value):
        if key in cls.__dict__:
            raise cls.ConstError('常量%s不能修改'%key)
        if not key.isupper():
            raise cls.ConstError('常量%s不能小写'%key)
        super().__setattr__(key, value)

    def __delattr__(cls, item):
        if item in cls.__dict__:
            raise cls.ConstError(f'常量{item}不能修改')
        super().__delattr__(item)


# sys.modules[__name__]=_const()
CONST = const()
CONST.PI = 3.14
# CONST.PI = 4
# print(CONST.PI)