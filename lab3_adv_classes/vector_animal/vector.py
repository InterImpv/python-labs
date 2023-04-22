#!/usr/bin/env python3.10

import cmath
import functools
import math

class Vector2D:
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x  # this attr (_x) was pseudoprivate

    @property
    def y(self):
        return self.__y  # this one is private (mangled)

    @property
    @functools.lru_cache(maxsize=1) # saves one recent call
    def length(self):
        return abs(self.x + 1j * self.y)

    @classmethod
    def from_polar(cls, length, angle, *, isdeg=True):
        """Make Vector from polar coordinates (length & angle)

        Args:
            length: vector length as returned by Vector.length
            angle: vector rotation in radians (if `isdeg` is False)
                   or in degrees (if `isdeg` is True or not provided)
            isdeg: angle is given in degrees (if True) or in radians
                   (if False)
        Returns:
            Vector instance
        """
        # do conversion to radians if needed
        if isdeg:
            angle = math.radians(angle)

        x = length * math.cos(angle)
        y = length * math.sin(angle)
        return cls(x=x, y=y)

    @staticmethod
    def angle_between(veca, vecb, *, isdeg=True):
        a, b = [vec.x + 1j * vec.y for vec in [veca, vecb]]
        anga, angb = [cmath.phase(el) for el in [a, b]]
        angle = angb - anga
        if isdeg:
            angle = math.degrees(angle)
        return angle

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __bool__(self):
        return not self.x == self.y == 0

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f'operands {self} and {other} type mismatch')

        # create a new vector with sum of coords
        x = self.x + other.x
        y = self.y + other.y
        # same as self.__class__(x=x, y=y)
        return type(self)(x=x, y=y)

    def __sub__(self, other):
        return self + (other * -1)  # call mul explicitly

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        # vector * scalar multiplication
        if not isinstance(other, type(self)):
            # if has other type
            if not isinstance(other, int):
                # and this type is not integer
                # ==> ensure it is convertable to float
                other = float(other)
            # now we're either dealing with int, or with float
            return type(self)(x=other * self.x, y=other * self.y)
        # vector * vector
        return (self.x * other.x + self.y * other.y)

    def __matmul__(self, other):
        # vector x vector, but this makes little sense
        return (self.x * other.y - self.y * other.x)

    def __truediv__(self, other):
        if not other:
            raise ZeroDivisionError

        return self * (1 / other)

    def __eq__(self, other):
        try:
            return self.x == other.x and self.y == other.y
        except Exception:
            return False

    # __neq__ is implemented automatically

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return [self.x, self.y][index]

    def __hash__(self):
        # if each object is unique
        # return id(self)
        # if it is not exactly unique and applicable to use
        # other object with same values during indexing
        return hash(self.x) ^ hash(self.y)

class Point(Vector2D):
    pass

if __name__ == '__main__':
    # basic constructors
    one = Vector2D(3, 5)
    two = Vector2D(10, 20)

    # mult (scalar), add, div (scalar)
    res = one * 3 + two / 10
    print(f'{one} * 3 + {two} / 10 = {res}\n')
    # dot product
    res = one * two
    print(f'{one} * {two} = {res}\n')
    # cross product
    res = one @ two
    print(f'{one} @ {two} = {res}\n')

    # null (zero) vector
    zero = Vector2D(0, 0)
    print(f'{zero}, bool(zero) = {bool(zero)}\n')  # returns False

    # diagonal
    diag = Vector2D.from_polar(length=10, angle=45, isdeg=True)
    print(f'diag = {diag}\n')

    # from polar
    one = Vector2D.from_polar(1, 45)
    two = Vector2D.from_polar(10, 135)
    print(f'from_polar = {one}, {two}\n')

    # angle between
    angle = Vector2D.angle_between(one, two)
    print(f'angle({one}, {two}) = {angle}\n')
