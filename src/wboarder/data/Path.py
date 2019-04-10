##  @package wboarder.data.Path
#
#   Contains the path class used to draw a picture

from src.wboarder.data.Point import Point


##  A path class used to draw an image
#
#   Is iterable
class Path:

    ##  Constructs an empty path object
    #
    def __init__(self):
        self._points = []
        self._index = 0
        self._length = 0

    ##  Adds the point given by (row, col) to the path object.
    #
    #   @param point a point being added to the path
    def addPoint(self, point : Point) -> None:
        self._points.append(point)
        self._length += 1

    ##
    #   Returns the size of the path
    def length(self):
        return self._length

    def __next__(self) -> Point:
        index = self._index
        if index == self._length:
            raise StopIteration
        else:
            next_entry = self._path._path[index]
            self._index += 1
            return next_entry

    def __iter__(self):
        return self
