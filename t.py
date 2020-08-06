import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# read cvs file
with open('c7.csv', newline='') as f:
  reader = csv.reader(f)
  data = list(reader)

# find *begin* place from input data
cnt_start = 0;
while(data[cnt_start][0] != 'Scan Start'):
  cnt_start+=1

# find *end* place from input data
cnt_end = 0;
while(data[cnt_end][0] != 'Scan End'):
  cnt_end+=1

# grab data from 'Scan Start' to 'Scan End' in input data with *begin* and *end* place
vals = []
for i in range(cnt_start +1 , cnt_end):
  vals.append(data[i])

# remove str '2d statistical'
vals[0].pop(0) 

# convert vals from string to float
for i in vals:
  for j in i:
    j = float(j)

# remove and grab column_vals(legend) from input data
column_vals = []
column_vals = vals.pop(0)

# remove and grab row_vals(legend) from input data
row_vals = []
for i in vals:
  row_vals.append(i.pop(0))

# convert vals to np arrau for plot
vals_arr = np.array(vals)

# initialize figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# create 2D meshgrid for plot
x_data, y_data = np.meshgrid( np.arange(vals_arr.shape[1]),
                              np.arange(vals_arr.shape[0]) )

# Flatten out the arrays so that they may be passed to "ax.bar3d".
# Basically, ax.bar3d expects three one-dimensional arrays:
# x_data, y_data, z_data. The following call boils down to picking
# one entry from each array and plotting a bar to from
# (x_data[i], y_data[i], 0) to (x_data[i], y_data[i], z_data[i]).
#
x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = vals_arr.flatten()


ax.bar3d( x_data,
          y_data,
          np.zeros(len(z_data)),
          1, 1, z_data )

plt.show()

#print (column_vals)
#print (row_vals)

#print(vals[2])
#print(vals)       
