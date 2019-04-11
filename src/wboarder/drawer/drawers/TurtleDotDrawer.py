##  @package wboarder.drawer.drawers.TurtleDotDrawer
#
#   Contains the TurtleDotDrawer class
#
#   \author Steven Maio

from src.wboarder.drawer.Drawer import Drawer
from src.wboarder.data.Board import Board
from src.wboarder.data.Path import Path
from src.wboarder.data.Point import Point

import turtle


##
#   Draws an image by creating dots at the points at which an object is set
class TurtleDotDrawer(Drawer):

    ## The default threshold for the ImageProcessor
    DEFAULT_THRESHOLD = 100
    ## The default distance between points
    DEFAULT_WIDTH = 5
    X_OFFSET = -300
    Y_OFFSET = -300

    def __init__(self):
        self._path = None
        self._board = None
        self._cell_width = TurtleDotDrawer.DEFAULT_WIDTH

    ##
    #   Initializes the TurtleDotDrawer
    #
    #   @param board the board representing the image
    #   @param path the path which the drawer must follow
    def init(self, board : Board, path : Path) -> None:
        self._path = path
        self._board = board

    ##
    #   Draws the image
    def draw(self) -> None:
        turtle.hideturtle()
        turtle.speed(0)
        turtle.up()
        points = self._path._points
        width = self._cell_width
        x_offset = TurtleDotDrawer.X_OFFSET
        y_offset = TurtleDotDrawer.Y_OFFSET
        for p in points:
            row = p.getRow()
            col = p.getCol()

            x = row*width + x_offset
            y = col*width + y_offset
            turtle.setposition(x, y)
            turtle.dot()
        turtle.exitonclick()
