from collections import namedtuple
from Point import Point3D

def index2mask(idx: int):
    return (idx&1, (idx>>1)&1, (idx>>2)&1)

def mask2index(idx: tuple):
    x, y, z = [int(bool(idx[i])) for i in range(3)]
    return (z<<2)+(y<<1)+x

def invMask(mask: tuple):
    return tuple([mask[i]^1 for i in range(3)])

class Octree():
    """Representation of a Node in the Octree."""
    def __init__(self, lower_bound: Point3D, upper_bound: Point3D, max_levels=-1, max_size=10):
        self.has_children = False
        self.children: Octree = []
        self.points: Point3D = []
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.max_levels = max_levels
        self.max_size = max_size
        self.center = (lower_bound + upper_bound) / 2
        self.numPoints = 0

    def extend(self):
        if (self.max_levels == 0):
            return
        else:
            self.has_children = True
            self.children = list([self._generateChildTree(idx) for idx in range(8)])

    def _generateChildTree(self, idx):
        mask = index2mask(idx)
        imask = invMask(mask)
        new_lower_bound = self.lower_bound*imask + self.center*mask
        new_upper_bound = self.center*imask + self.upper_bound*mask
        return Octree(new_lower_bound, new_upper_bound, self.max_levels - 1, self.max_size)

    def addPoint(self, pt: Point3D):
        if self.has_children:
            self._addPointToChild(pt)
        elif len(self.points) >= self.max_size:
            self.extend()
            for point in self.points:
                self._addPointToChild(point)
            self._addPointToChild(pt)
            self.points = []
        else:
            self.points.append(pt)
        self.numPoints += 1
       
    def _addPointToChild(self, pt: Point3D):
        x = int(pt.x >= self.center.x)
        y = int(pt.y >= self.center.y)
        z = int(pt.z >= self.center.z)
        self.children[mask2index((x, y, z))].addPoint(pt)