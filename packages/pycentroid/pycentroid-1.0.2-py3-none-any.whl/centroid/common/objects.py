from collections import namedtuple
from types import SimpleNamespace


class AnyObject(SimpleNamespace):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            if type(value) is dict:
                setattr(self, key, AnyObject(**value))
            elif type(value) is list:
                setattr(self, key, list(
                    map(lambda x: AnyObject(**x) if isinstance(x, dict) else x, value))
                        )

    def __getattr__(self, name):
        return self.__dict__.get(name, None)

    def __str__(self):
        return self.__dict__.__str__()


class AnyDict(dict):
    """A dictionary object which exports keys as attributes
    """
    def __init__(self, **kwargs):
        super(AnyDict, self).__init__()
        for key, value in kwargs.items():
            if type(value) is dict:
                self[key] = AnyDict(**value)
            elif isinstance(value, list):
                values = map(lambda x: AnyDict(**x) if type(x) is dict else x, value)
                self[key] = list(values)
            else:
                self[key] = value

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, name):
        return self.get(name, None)


def object(**kwargs):
    return AnyObject(**kwargs)


def dict_to_object(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = dict_to_object(v)
    return namedtuple('X', d.keys())(*d.values())
