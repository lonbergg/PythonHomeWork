class CamelCase(type):
    def __new__(cls, clsname, bases, clsdict):
        if not clsname[0].isupper():
            raise ValueError(f'Class name not in CamelCase: {clsname}')
        return super().__new__(cls, clsname, bases, clsdict)


class MyCamelCaseClass(metaclass=CamelCase):
    pass


class notCamelCase(metaclass=CamelCase):
    pass
