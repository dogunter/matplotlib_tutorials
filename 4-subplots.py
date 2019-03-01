import numpy as np
import matplotlib.pyplot as plt

# Continuing the 3-subplots.py examples.
# We create 4 subplots, 2 per row in 2 columns

# We want an array of 200 numbers from 0 to 2 Pi
# pi = 3.141592653.... is stored as a constant in numpy
x = np.linspace(0, 2*np.pi, num=200)

# The trig functions are defined in numpy, too.
# Now compute the function y1 = sin(x)
y1 = np.sin(x)

# Another function to plot: y2 = cos(x)
y2 = np.cos(x)

y3 = np.sin(x)*np.sin(x)
y4 = np.cos(x)*np.cos(x)

# Set up the plot
# plt.subplots() lets us create multiple plots in a figure if we wish.
# We want two plots on separate axes, in a single column
# ax will then be an array of axes
# Here we will set an explicit figure size (default in inches)
fig, ax = plt.subplots(2,2, figsize=(12,8))

# Set an overall figure title
fig.suptitle('A plot of the functions $f(x) = sin(x)$,  $f(x) = cos(x)$, $f(x) = sin^2(x)$, and $f(x) = cos^2(x)$', fontsize=14)

# Plot the values
# Note that ax is now a 2x2 matrix
ax[0][0].plot(x, y1, 'b', label='$sin(x)$')
ax[0][1].plot(x, y2, 'r', label='$cos(x)$')
ax[1][0].plot(x, y3, 'g', label='$sin^2(x)$')
ax[1][1].plot(x, y4, 'k', label='$cos^2(x)$')

# Label the x and y axes
# Since all the x-labels are the same, we do this in a loop
for i in range(2):
    for j in range(2):
        ax[i][j].set_xlabel('x')

ax[0][0].set_ylabel('$sin(x)$')
ax[0][1].set_ylabel('$cos(x)$')
ax[1][0].set_ylabel('$sin^2(x)$')
ax[1][1].set_ylabel('$cos^2(x)$')

# Now we have to set the spines for each of the axes
# All spines will be the same, so use the loop method again
for i in range(2):
    for j in range(2):
        ax[i][j].spines['left'].set_position(('data', -0.2))
        ax[i][j].spines['right'].set_color('none')
        ax[i][j].spines['bottom'].set_position(('data', 0))
        ax[i][j].spines['top'].set_color('none')
        ax[i][j].xaxis.set_ticks_position('bottom')
        ax[i][j].yaxis.set_ticks_position('left')

# Display the plot
plt.show()

