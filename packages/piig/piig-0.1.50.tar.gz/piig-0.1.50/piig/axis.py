import typing

from enum import IntEnum


class Axis(IntEnum):
    X = 0
    Y = 1
    Z = 2
    A = 3
    B = 4
    C = 5
    U = 6
    V = 7
    W = 8

    @property
    def lname(self):
        return self.name.lower()

    # @property
    # def bname(self):
    #     return self.name

    # @property
    # def dotname(self):
    #     return "." + self.lname

    # def __repr__(self):
    #     return self.lname

    #    @property
    #    def mat(self):


#        return MAT[self.value]
lnames = [axis.lname for axis in Axis]
name_to_index = {axis.lname: axis.value for axis in Axis}
name_to_index.update({axis.value: axis.value for axis in Axis})


# def axis_ch_to_idx(name: str) -> int:
#     return name_to_index[name]


def name_to_indexes(name: str) -> typing.Generator[int, None, None]:
    #   try:
    try:
        for ch in name:
            a = name_to_index[ch]
            yield a
    except KeyError as exc:
        raise AttributeError from exc


#    except KeyError:
#        breakpoint()
#        exception.rErrorHere(f"Bad axis name {name}")


X = Axis.X
Y = Axis.Y
Z = Axis.Z
