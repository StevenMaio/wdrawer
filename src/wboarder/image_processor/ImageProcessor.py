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

    ##  Abstract method. Sets the path to the image, but however that's
    #   handled is up to the implementation of ImageProcessor
    #
    #   @param image_path the path to the image.
    @abstractmethod
    def setImage(image_path : str) -> None:
        raise NotImplementedError
