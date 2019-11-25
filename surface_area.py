#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program calculates the surface area of a sphere

import math


def calculate_surface_area(radius):
    # calculate surface area
    # process
    surface_area = 4 * math.pi * radius ** 2
    # output
    print("Surface area is {:.2f} cm3".format(surface_area))
    return surface_area


def main():
    # this function gets radius and height
    while True:
        # input
        radius_user_input = input("Enter the Radius of The sphere (cm): ")
        print("")

        # process
        try:
            radius_from_user_int = int(radius_user_input)
            print("Valid Input")
            # call functions
            calculate_surface_area(radius_from_user_int)

        # Prevents the program from crashing
        except ValueError:
            print("Not An Integer")
            continue

        else:
            break


if __name__ == "__main__":
    main()
