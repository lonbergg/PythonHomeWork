class NoDunderAttributes(type):
    def __new__(cls, clsname, bases, clsdict):
        for attr_name in clsdict:
            if attr_name.startswith('__') and attr_name.endswith('__'):
                raise ValueError(f'Cannot have attribute names starting with "__": {attr_name}')
        return super().__new__(cls, clsname, bases, clsdict)


class MyPrivateClass(metaclass=NoDunderAttributes):
    __secret_attribute = 10
