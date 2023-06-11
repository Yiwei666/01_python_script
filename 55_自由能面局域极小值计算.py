# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:45:30 2023

@author: sun78
"""

def find_min_z_and_corresponding_y(x_min, x_max, file_name):
    """
    This function finds the minimum value of z for a specified x value range,
    and prints the minimum value of z, y value corresponding to the minimum z, 
    and the product of minimum z with 4.3597*6.022*100.

    Parameters:
    x_min (float): Minimum value of x for which z needs to be found.
    x_max (float): Maximum value of x for which z needs to be found.
    file_name (str): Name of the data file.

    Returns:
    None
    """
    min_z = None
    min_y = None
    with open(file_name, 'r') as f:
        for line in f:
            x, y, z = line.split()
            x = float(x)
            y = float(y)
            z = float(z)
            if x_min <= x <= x_max:
                if min_z is None or z < min_z:
                    min_z = z
                    min_y = y
    if min_z is not None:
        print("Minimum z value for x in range [{}, {}]: {}".format(x_min, x_max, min_z))
        print("Corresponding y value: {}".format(min_y))
        print("Product of minimum z with 4.3597*6.022*100: {}".format(min_z*4.3597*6.022*100))
    else:
        print("No data found for x in range [{}, {}]".format(x_min, x_max))


find_min_z_and_corresponding_y(0, 2, 'fes.dat')
