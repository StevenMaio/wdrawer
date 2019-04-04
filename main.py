##  @package wboarder
#
#   \author Steven Maio

import argparse


def main(**kwargs):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="An argument parser")
    args = vars(parser.parse_args())
    main(**args)
