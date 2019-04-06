##  @package wboarder.drawer.drawers.PrintDrawer
#
#   Contains the PrintDrawer class
#
#   \author Steven Maio

from src.wboarder.drawer.Drawer import Drawer


##  Drawer implementation which prints the points of the path to system out
#   in the order in which they were added
class PrintDrawer(Drawer):

    ##  Constructs an empty PrintDrawer instance
    #
    def __init__(self):
        self._path = None

    ##  Initializes the PrintDrawer instance
    #
    #   @param board the board from which the path was created
    #   @param path the path which PrintDrawer will 'draw'
    def init(self, board : Board, path : Path) -> None:
        self._path = path

    ##  Prints out the points in path in sequence
    #
    def draw(self) -> None:
        for p in self._path:
            print(p)
