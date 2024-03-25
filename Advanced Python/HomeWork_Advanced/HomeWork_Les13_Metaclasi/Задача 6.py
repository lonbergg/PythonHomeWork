class LoggingMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        print(f'Class "{clsname}" has been created')
        return super().__new__(cls, clsname, bases, clsdict)


class MyClass(metaclass=LoggingMeta):
    pass
