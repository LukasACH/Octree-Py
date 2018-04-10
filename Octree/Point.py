from math import sqrt


class Point3D():
    """A point in 3 dimensions"""
    def __init__(self, x, y, z, data=None):
        self.x = x
        self.y = y
        self.z = z
        self.data = data

    def __add__(self, point):
        return Point3D(self.x + point.x, self.y + point.y, self.z + point.z)

    def __sub__(self, point):
        return Point3D(self.x - point.x, self.y - point.y, self.z - point.z)

    def __mul__(self, value):
        if type(value) == tuple:
            return Point3D(self.x * value[0], self.y * value[1], self.z * value[2])
        else:
            return Point3D(self.x * value, self.y * value, self.z * value)


    def __truediv__(self, value):
        if type(value) == Point3D:
            raise NotImplementedError()
        else:
            return Point3D(self.x / value, self.y / value, self.z / value)

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(x='+str(self.x)+', y='+str(self.y)+', z='+str(self.z)+')'

    def dist(self, point):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
