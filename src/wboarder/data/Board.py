##  @package wboarder.data.Board
#
#   Contains the Board class
#
#   \author Steven Maio

from src.wboarder.data.Point import Point


## A board object representing the data in the image
#
class Board:

    ##  Constructs an empty board with **num_rows** rows and **num_cols** columns.
    #   
    #   Initializes an empty board, in which the default value for every entry
    #   is 0.
    #
    #   @param num_cols the number of columns in the board
    #   @param num_rows the number of rows in the board
    #   @param default_value the default value to assign to each row
    def __init__(self, num_rows : int, num_cols : int, default_value : object):
        self._num_rows = num_rows
        self._num_cols = num_cols
        points = []
        for i in range(num_rows):
            rows = []
            for j in range(num_cols):
                rows.append(default_value)
            points.append(rows)
        self._points = points

    ##  Returns the number of rows on the board
    #
    #   @return an integer value indicating the total number of rows
    def getNumRows(self) -> int:
        return self._num_rows

    ## Returns the number of rows on the board
    #
    #   @return an integer value indicating the total number of columns
    def getNumCols(self) -> int:
        return self._num_cols

    ##  Accessor method for the board. Returns the value at location (row, col)
    #   on the board.
    #
    #   @param row the row number of the entry
    #   @param col the column number of the entry
    #   @return the float value stored at row,col
    def get(self, point : Point) -> object:
        row = point.getRow()
        col = point.getCol()
        if 0 <= row < self._num_rows and 0 <= col < self._num_cols:
            return self._points[row][col]
        else:
            raise ValueError("illegal value for row or col")

    ##  Mutator method for the board. Sets the value at location (row, col) to
    #   value 
    #
    #   @param row the row number of the entry being modified
    #   @param col the column number of the entry being modified
    #   @param value the new value of the entry being modified
    def set(self, row : int, col : int, value : object) -> None:
        if 0 <= row < self._num_rows and 0 <= col < self._num_cols:
            self._points[row][col] = value
        else:
            raise ValueError("illegal value for row or col")
