##  @package wboarder
#
#   Starting point of the application. Parses arguments and initializes
#   the configuration for the program.
#
#   \author Steven Maio

from src.wboarder.configuration.configurations import *

import argparse
import src.wboarder.wboarder as wboarder
import importlib


def main(image : str, configuration : str, args : list) -> None:
    config = None
    wboarder.start(image=image, configuration=config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draws an image")
    parser.add_argument("image",
                        type=str,
                        help="image being processed by wboarder")
    parser.add_argument("configuration",
                        type=str,
                        help="path to the configuration module being used")
    parser.add_argument("args",
                        type=str,
                        nargs=argparse.REMAINDER,
                        help="configuration arguments")
    args = vars(parser.parse_args())
    main(**args)
