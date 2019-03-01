import numpy as np
import matplotlib.pyplot as plt

# A demonstration of how to plot multple plots
# with different axes in the same figure,
# using subplots9)

# We want an array of 200 numbers from 0 to 2 Pi
# pi = 3.141592653.... is stored as a constant in numpy
x = np.linspace(0, 2*np.pi, num=200)

# The trig functions are defined in numpy, too.
# Now compute the function y1 = sin(x)
y1 = np.sin(x)

# Another function to plot: y2 = cos(x)
y2 = np.cos(x)

# Set up the plot
# plt.subplots() lets us create multiple plots in a figure if we wish.
# We want two plots on separate axes, in a single column
# ax will then be an array of axes
fig, ax = plt.subplots(2,1)

# Set an overall figure title
fig.suptitle('A plot of the functions $f(x) = sin(x)$ and $f(x) = cos(x)$', fontsize=14)

# Plot the values
ax[0].plot(x, y1, 'b', label='$sin(x)$')
ax[1].plot(x, y2, 'r', label='$cos(x)$')

# Label the x and y axes
ax[0].set_xlabel('x')
ax[0].set_ylabel('$sin(x)$')
ax[1].set_xlabel('x')
ax[1].set_ylabel('$cos(x)$')

# Now we have to set the spines for each of the axes
# Full documentation can be read about "spines" here:
# https://matplotlib.org/examples/pylab_examples/spine_placement_demo.html
ax[0].spines['left'].set_position(('data', -0.2))
ax[0].spines['right'].set_color('none')
ax[0].spines['bottom'].set_position(('data', 0))
ax[0].spines['top'].set_color('none')
ax[0].xaxis.set_ticks_position('bottom')
ax[0].yaxis.set_ticks_position('left')

ax[1].spines['left'].set_position(('data', -0.2))
ax[1].spines['right'].set_color('none')
ax[1].spines['bottom'].set_position(('data', 0))
ax[1].spines['top'].set_color('none')
ax[1].xaxis.set_ticks_position('bottom')
ax[1].yaxis.set_ticks_position('left')

# Display the plot
plt.show()

