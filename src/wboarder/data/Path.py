##  @package wboarder.data.Path
#
#   Contains the path class used to draw a picture

from src.wboarder.data.Point import Point


##  A path class used to draw an image
#
#   Is iterable
class Path:

    #   Nested iterator class. Iterates over the points in a path.
    #
    class PathIterator:

        def __init__(self, path):
            self._index = 0
            self._path = path
            self._length = len(path._points)

        def next(self) -> Point:
            index = self._index
            if index == self._length:
                raise StopIteration
            else:
                nextEntry = self._path._path[index]
                self._index += 1

    ##  Constructs an empty path object
    #
    def __init__(self):
        self._points = []

    ##  Adds the point given by (row, col) to the path object.
    #
    #   @param point a point being added to the path
    def addPoint(self, point : Point) -> None:
        self._points.append(point)

    def __iter__(self) -> PathIterator:
        return PathIterator(path=self)
