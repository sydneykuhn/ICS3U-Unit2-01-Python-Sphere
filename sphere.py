#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the area and perimeter of a sphere
#    with the radius of 15 mm

import math


def main():
    # this function calculates area and perimeter

    print("If a circle has a radius of 15mm:")
    print("")
    print("Area is {}mm2.".format(4 * math.pi * 15 ** 2))
    print("Perimeter is {}mm.".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
