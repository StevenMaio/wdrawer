##  @package wboarder.configuation.Configuratoin
#
#   Contains the Configuratoin class
#
#   \author Steven Maio

from src.wboarder.image_processor.ImageProcessor import ImageProcessor
from src.wboarder.drawer.Drawer import Drawer
from src.wboarder.pather.Pather import Pather

from abc import ABC, abstractmethod

##  A configuration object. Must be implemented by the user for a custom
#   drawing.
#
class Configuration(ABC):

    ##  Returns the ImageProcessor used by the configuation
    #
    #   @return an instance of ImageProcessor
    @abstractmethod
    def initImageProcessor(self) -> ImageProcessor:
        raise NotImplementedError

    ##  Returns the Pather used in the scenario
    #
    #   @return a Pather instance uesd to create the path followed by the
    #   Drawer
    @abstractmethod
    def initPather(self) -> Pather:
        raise NotImplementedError

    ##  Returns the Drawer used to create the image defined by the Pather
    #
    #   @return a Drawer instance used to create the image
    @abstractmethod
    def initDrawer(self) -> Drawer:
        raise NotImplementedError
