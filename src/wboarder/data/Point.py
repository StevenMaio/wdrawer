##  @package wboarder.data.Point
#
#   Contains the Point class
#
#   \author Steven Maio


## A point object in the plane.
#
class Point:

    ##  Constructs a new point object with initial values for row and col
    #
    #   @param row the row number of the point
    #   @param col the column number of the point
    def __init__(self, row : int, col : int):
        self._row = row
        self._col = col

    ##  Accessor method for the row field
    #
    #   @return an integer value indicating the row number of the point
    def getRow(self) -> int:
        return self._row

    ##  Accessor method for the col field
    #
    #   @return an integer value indicating the column number of the point
    def getCol(self) -> int:
        return self._col

    def __str__(self):
        print("({},{})".format(self._row, self._col))
