import matplotlib.pyplot as plt
import numpy as np

def find_and_plot_min_z_in_grids(file_name):
    """
    This function reads a data file and finds the minimum value of z within each 1x1 grid over the entire range
    of x and y provided in the file. It then plots a 2D grid where each cell's color indicates the magnitude
    of the minimum z found within that cell, and each cell displays the x, y, z coordinates of the point
    where the minimum z occurs, displayed over three lines for readability. The z-value is scaled by
    a constant factor (4.3597*6.022*100) before displaying.

    Parameters:
    file_name (str): Name of the data file containing x, y, z values.

    Returns:
    None
    """
    # Initialize containers for data and bounds
    data = []
    x_min, x_max, y_min, y_max = float('inf'), -float('inf'), float('inf'), -float('inf')

    # Read data and determine the bounds
    with open(file_name, 'r') as f:
        for line in f:
            x, y, z = map(float, line.split())
            data.append((x, y, z))
            if x < x_min:
                x_min = x
            if x > x_max:
                x_max = x
            if y < y_min:
                y_min = y
            if y > y_max:
                y_max = y

    # Initialize dictionary to store min z and corresponding x, y in each grid
    grid_min_z = {}
    for x in range(int(x_min), int(x_max) + 1):
        for y in range(int(y_min), int(y_max) + 1):
            grid_min_z[(x, y)] = {'z': float('inf'), 'x': None, 'y': None}

    # Update minimum z values in each corresponding grid
    for x, y, z in data:
        grid_x = int(x)
        grid_y = int(y)
        if z < grid_min_z[(grid_x, grid_y)]['z']:
            grid_min_z[(grid_x, grid_y)] = {'z': z, 'x': x, 'y': y}

    # Prepare data for plotting
    num_x = int(x_max) - int(x_min) + 1
    num_y = int(y_max) - int(y_min) + 1
    z_values = np.full((num_y, num_x), np.nan)
    labels = np.full((num_y, num_x), "", dtype=object)

    for key, value in grid_min_z.items():
        if value['z'] != float('inf'):
            ix = key[0] - int(x_min)
            iy = key[1] - int(y_min)
            scaled_z = value['z'] * 4.3597 * 6.022 * 100
            z_values[iy, ix] = scaled_z
            labels[iy, ix] = f"{value['x']:.1f}\n{value['y']:.1f}\n{scaled_z:.1f}"


    # Create a figure with high resolution
    fig, ax = plt.subplots(dpi=600)  # Set dpi to 300 for high resolution
    cax = ax.matshow(z_values, cmap='viridis', origin='lower')
    
    # Add text annotations with scaled z values
    for (i, j), label in np.ndenumerate(labels):
        if label:
            ax.text(j, i, label, va='center', ha='center', color='white', fontsize=4)  # Adjust fontsize as needed
    
    # Add colorbar and labels
    fig.colorbar(cax)
    plt.xticks(range(num_x), range(int(x_min), int(x_max) + 1))
    plt.yticks(range(num_y), range(int(y_min), int(y_max) + 1))
    plt.tick_params(axis='both', which='both', length=0)  # Hide tick marks, keep labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.xaxis.tick_bottom()  # Ensure ticks are on the bottom for x-axis
    plt.title('Scaled minimum z values in each grid')
    plt.show()

# Call the function with the file name
find_and_plot_min_z_in_grids('fes.dat')
