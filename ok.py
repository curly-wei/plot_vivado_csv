#! /usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#
# Assuming you have "2D" dataset like the following that you need
# to plot.
#
data_2d = [ [1.1, 2.5, 3.5, 4.6, 5.5, 6.6, 7.2, 8.1, 9.5, 10.1],
            [6.1, 7.9, 8.1, 9.1, 10.1, 11.1, 12.1, 13.1, 14.9, 15.8],
            [11.5, 12.7, 13.8, 14.7, 15.5, 16.2, 17.4, 18.6 , 19.5, 20.1],
            [16.8, 17.8, 18.8, 19.4, 20.8, 21.8, 22.7, 23.5, 24.8, 25.1],
            [21.7, 22.5, 23.2, 24.2, 25.4, 26.7, 27.5, 28.1, 29.1, 30.4] ]
#
# Convert it into an numpy array.
#
data_array = np.array(data_2d)
#
# Create a figure for plotting the data as a 3D histogram.
#
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#
# Create an X-Y mesh of the same dimension as the 2D data. You can
# think of this as the floor of the plot.
#
x_data, y_data = np.meshgrid( np.arange(data_array.shape[1]),
                              np.arange(data_array.shape[0]) )
#
# Flatten out the arrays so that they may be passed to "ax.bar3d".
# Basically, ax.bar3d expects three one-dimensional arrays:
# x_data, y_data, z_data. The following call boils down to picking
# one entry from each array and plotting a bar to from
# (x_data[i], y_data[i], 0) to (x_data[i], y_data[i], z_data[i]).
#
x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = data_array.flatten()
ax.bar3d( x_data,
          y_data,
          np.zeros(len(z_data)),
          1, 1, z_data )
#
# Finally, display the plot.
#
plt.show()


