##  @package wboarder.pather.LeftToRightPather
#
#   Contains the LeftToRightPather
#
#   \author Steven Maio

from src.wboarder.pather.Pather import Pather
from src.wboarder.data.Path import Path
from src.wboarder.data.Point import Point
from src.wboarder.data.Board import Board


##  Creates a path which goes from left to right
#
class LeftToRightPather(Pather):

    ##  Creates a Path object from a given instance of a Board, which moves
    #   left to right on each row.
    #
    #   @return a path object
    def createPath(self, board : Board) -> Path:
        path = Path()
        num_rows = board.getNumRows()
        num_cols = board.getNumCols()
        for row in range(num_rows):
            for col in range(num_cols):
                p = Point(row=row, col=col)
                value = board.get(point=p)
                if value > 0:
                    path.addPoint(point=p)
        return path
