##  @package wboarder.pather.Pather
#
#   Contains the abstract Pather class
#
#   \author Steven Maio

from src.wboarder.data.Board import Board
from src.wboarder.data.Path import Path

from abc import ABC, abstractmethod


##  Abstract class
#
#   Creates a path to be followed by a drawer.
class Pather(ABC):

    ##  Abstract method. Creates a path based on some algorithm used by a
    #   descendant of Drawer to draw an image.
    #
    #   @return a path object that a drawer uses to draw 
    @abstractmethod
    def createPath(self, board : Board) -> Path:
        raise NotImplementedError
