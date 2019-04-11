##  @package wboarder.configuration.configurations.TurtlePlainConfig
#
#   Contains the TurtlePlainConfig class. Uses LeftToRightPather and
#   TurtleDotDrawer.
#
#   \author Steven Maio

from src.wboarder.configuration.Configuration import  Configuration
from src.wboarder.configuration.configurations.PlainConfiguration import PlainConfiguration
from src.wboarder.image_processor.ImageProcessor import ImageProcessor
from src.wboarder.image_processor.processors.DiscreteProcessor import DiscreteProcessor
from src.wboarder.drawer.Drawer import Drawer
from src.wboarder.drawer.drawers.TurtleDotDrawer import TurtleDotDrawer
from src.wboarder.pather.LeftToRightPather import LeftToRightPather
from src.wboarder.pather.Pather import Pather

import argparse


##  A simple implementation of the Configuration class.
#
class TurtlePlainConfig(Configuration):

    ## The default threshold for the ImageProcessor
    DEFAULT_THRESHOLD = 100

    def __init__(self):
        self._threshold = TurtlePlainConfig.DEFAULT_THRESHOLD

    ##  Overrided init method. For this implementation, this method is not
    #   necessary
    #
    #   @param args a list of arguments to the constructor
    def init(self, args : list) -> None:
        parser = argparse.ArgumentParser()
        parser.add_argument("--threshold",
                            "-t",
                            type=float,
                            default=PlainConfiguration.DEFAULT_THRESHOLD,
                            help="the threshold used to limit to test a point")
        config_args = vars(parser.parse_args(args))
        self._threshold = config_args.get("threshold")

    ##  Returns a basic ImageProcessor implementation
    #
    #   @return an instance of ImageProcessor
    def initImageProcessor(self) -> ImageProcessor:
        processor = DiscreteProcessor()
        processor.setThreshold(self._threshold)
        return processor

    ##  Returns an instance of LeftToRightPather
    #
    #   @return an instance of LeftToRightPather
    def initPather(self) -> Pather:
        return LeftToRightPather()

    ##  Returns an instace of PrintDrawer
    #
    #   @return an instance of PrintDrawer
    def initDrawer(self) -> Drawer:
        return TurtleDotDrawer()

##  Creates a new instance of the TurtlePlainConfig class
#
#   @return a TurtlePlainConfig instance
def createConfiguration() -> TurtlePlainConfig:
    return TurtlePlainConfig()
