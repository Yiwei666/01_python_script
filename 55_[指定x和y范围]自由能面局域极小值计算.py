# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:26:28 2023

@author: sun78
"""

def find_min_z_and_corresponding_x_and_y(x_min, x_max, y_min, y_max, file_name):
    """
    This function finds the minimum value of z for a specified x value range and y value range,
    and prints the minimum value of z, x value corresponding to the minimum z, 
    y value corresponding to the minimum z, and the product of minimum z with 4.3597*6.022*100.

    Parameters:
    x_min (float): Minimum value of x for which z needs to be found.
    x_max (float): Maximum value of x for which z needs to be found.
    y_min (float): Minimum value of y for which z needs to be found.
    y_max (float): Maximum value of y for which z needs to be found.
    file_name (str): Name of the data file.

    Returns:
    None
    """
    min_z = None
    min_x = None
    min_y = None
    with open(file_name, 'r') as f:
        for line in f:
            x, y, z = line.split()
            x = float(x)
            y = float(y)
            z = float(z)
            if (x_min <= x <= x_max) and (y_min <= y <= y_max):
                if min_z is None or z < min_z:
                    min_z = z
                    min_x = x
                    min_y = y
    if min_z is not None:
        print("Minimum z value for x in range [{}, {}] and y in range [{}, {}]: {}".format(x_min, x_max, y_min, y_max, min_z))
        print("Corresponding x value: {}".format(min_x))
        print("Corresponding y value: {}".format(min_y))
        print("Product of minimum z with 4.3597*6.022*100: {}".format(min_z*4.3597*6.022*100))
    else:
        print("No data found for x in range [{}, {}] and y in range [{}, {}]".format(x_min, x_max, y_min, y_max))


find_min_z_and_corresponding_x_and_y(4, 10, -1, 1, 'fes.dat')
