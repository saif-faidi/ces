import json


def color_bounds_setter(fn):
    def inner(self, value):
        if value > 255:
            value = 255
        elif value < 0:
            value = 0
        fn(self, value)

    return inner


class Color:
    def __init__(self, id, r, g, b, intensity):
        self.r = r
        self.g = g
        self.b = b
        self.intensity = intensity
        self.id = id

    def __repr__(self):
        return json.dumps(self.to_json(), indent=4)

    @property
    def r(self):
        return self.__r

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__b

    @property
    def intensity(self):
        return self.__intensity

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @r.setter
    @color_bounds_setter
    def r(self, value):
        self.__r = value

    @g.setter
    @color_bounds_setter
    def g(self, value):
        self.__g = value

    @b.setter
    @color_bounds_setter
    def b(self, value):
        self.__b = value

    @intensity.setter
    @color_bounds_setter
    def intensity(self, value):
        self.__intensity = value

    def to_json(self):
        return {
            'id': self.__id,
            'r': self.__r,
            'g': self.__g,
            'b': self.__b,
            'intensity': self.__intensity,
        }


class ColorStrip(Color):

    def __init__(self, id : int, r, g, b, intensity ) -> None:
        super(ColorStrip, self).__init__(id,r,g,b,intensity)

    def to_json(self):
        return {
            'strip':{
                **super().to_json()
            }
        }


class ColorEFI(Color):
    def __init__(self, id, r, g, b, intensity):
        super(ColorEFI, self).__init__(id,r,g,b,intensity)

    def to_json(self):
        return {
            'efi':{
                **super().to_json()
            }
        }
