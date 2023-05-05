# PythonProperty
# Python’s property() is the Pythonic way to avoid formal getter and setter methods in your code. This function allows you to turn class attributes into properties or managed attributes

# Providing Read-Only Attributes
# Probably the most elementary use case of property() is to provide read-only attributes in your classes. Say you need an immutable Point class that doesn’t allow the user to mutate the original value of its coordinates, x and y. 
# To achieve this goal, you can create Point like in the following example:

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


point = Point(12, 5)

# Read coordinates
point.x
# 12
point.y
# 5
# Write coordinates
point.x = 42
# The above assigning statement will throw error. Traceback (most recent call last):
# AttributeError: can't set attribute


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return round(math.dist((0, 0), (self.x, self.y)))

    @property
    def angle(self):
        return round(math.degrees(math.atan(self.y / self.x)), 1)

    def as_cartesian(self):
        return self.x, self.y

    def as_polar(self):
        return self.distance, self.angle

point = Point(12, 5)

point.x
point.y
point.distance
point.angle
# Calling method differs for functions/variable with property set and without.
point.as_cartesian()

point.as_polar()