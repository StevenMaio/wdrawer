##  @package wboarder.configuration.configurations.PlainConfiguration
#
#   Contains the PlainConfiguration class. Uses LeftToRightPather and
#   PrintDrawer.
#
#   \author Steven Maio

from src.wboarder.configuration.Configuration import  Configuration
from src.wboarder.image_processor.ImageProcessor import ImageProcessor
from src.wboarder.drawer.Drawer import Drawer
from src.wboarder.drawer.drawers.PrintDrawer import PrintDrawer
from src.wboarder.pather.LeftToRightPather import LeftToRightPather
from src.wboarder.pather.Pather import Pather


##  A simple implementation of the Configuration class.
#
class PlainConfiguration(Configuration):

    def __init__(self):
        pass

    ##  Overrided init method. For this implementation, this method is not
    #   necessary
    #
    #   @param args a list of arguments to the constructor
    def init(self, args : list) -> None:
        pass

    ##  Returns a basic ImageProcessor implementation
    #
    #   @return an instance of ImageProcessor
    def initImageProcessor(self) -> ImageProcessor:
        pass

    ##  Returns an instance of LeftToRightPather
    #
    #   @return an instance of LeftToRightPather
    def initPather(self) -> Pather:
        return LeftToRightPather()

    ##  Returns an instace of PrintDrawer
    #
    #   @return an instance of PrintDrawer
    def initDrawer(self) -> Drawer:
        return PrintDrawer()

##  Creates a new instance of the PlainConfiguration class
#
#   @return a PlainConfiguration instance
def createConfiguration() -> PlainConfiguration:
    return PlainConfiguration()
