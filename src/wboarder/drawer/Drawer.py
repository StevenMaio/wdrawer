##  @package wboarder.drawer.Drawer
#
#   Contains the abstract Drawer class
#
#   \author Steven Maio

from src.wboarder.data.Board import Board
from src.wboarder.data.Path import Path

from abc import ABC, abstractmethod


##  Abstract drawing class.
#
#   Draws an imagine using the abstract methods
class Drawer(ABC):

    ##  Abstract method.
    #
    #   Initializes drawer instance
    @abstractmethod
    def init(self, board : Board, path : Path) -> None:
        raise NotImplementedError

    ##  Abstract method
    #
    #   Draws a object based
    @abstractmethod
    def draw(self) -> None:
        raise NotImplementedError
