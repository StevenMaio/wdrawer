##  @package wboarder.image_processor.processors.DiscreteProcessor
#
#   Contains the DiscreteProcessor class
#
#   \author Steven Maio

from src.wboarder.image_processor.ImageProcessor import ImageProcessor


##
#   An implementation of the ImageProcessor class. Depending on a set
#   threshold, the DiscreteProcessor either set the values of the board
#   to 0 or 1.
#
#   TODO : implement this class
class DiscreteProcessor(ImageProcessor):

    ## Indicates that the space on the board is empty
    EMPTY = 0
    ## Indicates that the space on the board is not empty
    NON_EMPTY = 1

    ##
    #   Constructs a new instance of the DiscreteProcessor class
    def __init__(self):
        pass

    ##
    #   Creates a board instance from the data input
    def processImage(self) -> Board:
        pass

    ##
    #   Sets the image to be processed by the DiscreteProcessor
    #
    #   @param image_path the path to the image file
    def setImage(self, image_path : str) -> None
        pass
