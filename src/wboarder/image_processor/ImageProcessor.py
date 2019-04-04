##  @package wboarder.image_processor.ImageProcessor
#
#   Contains the ImageProcessor class
#
#   \author Steven Maio 

from src.wboarder.data.Board import Board

from abc import ABC, abstractmethod


##  Abstract class
#
#   Processes an image and creates a Board object from it
class ImageProcessor(ABC):

    ##  Abstract method. Processes an image into a Board object
    #
    #   @return a Board object based on the image
    @abstractmethod
    def processImage(self) -> Board:
        raise NotImplementedError
