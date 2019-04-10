##  @package wboarder
#
#   \author Steven Maio

from src.wboarder.configuration.Configuration import Configuration


##  Starts the application
#
#   @param configuration the configuration of the application
def start(configuration : Configuration, image : str) -> None:
    image_processor = configuration.initImageProcessor()
    pather = configuration.initPather()
    drawer = configuration.initDrawer()
    image_processor.setImage(image)
    board = image_processor.processImage()
    path = pather.createPath(board=board)
    drawer.init(board=board, path=path)
    drawer.draw()
