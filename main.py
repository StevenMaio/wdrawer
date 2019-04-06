##  @package wboarder
#
#   \author Steven Maio

import argparse


def main(image : str, configuration : str, args : list) -> None:
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draws an image")
    parser.add_argument("image",
                        type=str,
                        help="image being processed by wboarder")
    parser.add_argument("configuration",
                        type=str,
                        help="configuration used by wboarder")
    parser.add_argument("args",
                        type=str,
                        nargs=argparse.REMAINDER,
                        help="configuration arguments for the configuration object")
    args = vars(parser.parse_args())
    print(args)
    main(**args)
