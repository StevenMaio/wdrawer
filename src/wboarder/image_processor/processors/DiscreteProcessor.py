##  @package wboarder.image_processor.processors.DiscreteProcessor
#
#   Contains the DiscreteProcessor class
#
#   \author Steven Maio

from src.wboarder.image_processor.ImageProcessor import ImageProcessor
from src.wboarder.data.Board import Board

from PIL import Image
from types import LambdaType


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
    NOT_EMPTY = 1
    ## The default threshold used to determine if a space is empty or not
    DEFAULT_THRESHOLD = 100
    ## Test function

    MAX_FUNCTION = lambda r,g,b : max(r,g,b)

    ##
    #   Constructs a new instance of the DiscreteProcessor class. Sets the
    #   threshold value to DEFAULT_THRESHOLD.
    def __init__(self):
        self._image = None
        self._threshold = DiscreteProcessor.DEFAULT_THRESHOLD
        self._value_function = DiscreteProcessor.MAX_FUNCTION

    ##
    #   Creates a board instance from the data input
    #
    #   @return an instance of board which represents the processed image
    def processImage(self) -> Board:
        image = self._image
        num_cols, num_rows = image.size
        board = Board(num_rows=num_rows,
                      num_cols=num_cols,
                      default_value=DiscreteProcessor.EMPTY)
        # Iterate over each pixel in the image, and determine the threshold
        f = self._value_function
        threshold = self._threshold
        for row in range(num_rows):
            for col in range(num_cols):
                r,g,b = image.getpixel((col, row))
                val = f(r,g,b)
                if val <= threshold:
                    board.set(row=row,
                              col=col,
                              value=DiscreteProcessor.NOT_EMPTY)
        return board

    ##
    #   Sets the image to be processed by the DiscreteProcessor
    #
    #   @param image_path the path to the image file
    def setImage(self, image_path : str) -> None:
        # create an instance of PIL.image
        self._image = Image.open(image_path)

    ##
    #   Sets the value of the threshold
    #
    #   @param threshold the value used to determine if the pixel is 'empty'
    #          or not
    def setThreshold(self, threshold : float) -> None:
        self._threshold = threshold

    ##
    #   Sets the test function
    #
    #   @param f an anonymous function of the form lambda r,g,b where r,g,b
    #          correspond to the RGB values of each pixel
    def setValueFunction(self, f : LambdaType) -> None:
        self._value_function = f
