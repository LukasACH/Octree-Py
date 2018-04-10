from Octree import *
from Point import Point3D

from random import random


ot = Octree(Point3D(0, 0, 0), Point3D(1, 1, 1))


for i in range(10000):
    ot.addPoint(Point3D(random(), random(), random()))
