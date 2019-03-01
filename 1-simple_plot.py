import numpy as np
import matplotlib.pyplot as plt

# numpy's linspace function returns an evenly spaced array
# of numbers over a specified interval.
# ex) x = np.linspace(10,20, num=10)
#     Returns 5 numbers between 10 and 20:
#     >>> x
#     array([10. , 12.5, 15. , 17.5, 20. ])
#
#
# We want an array of 200 numbers from -5 to +5
x = np.linspace(-5, 5, num=200)

# Now compute the function y = x^2 
y = x*x

# Set up the plot
# plt.subplots() lets us create multiple plots in a figure if we wish.
# The arguments specify the number of rows and columns. We only need 1.
# 'fig' is the overall figure in which we will plot.
# 'ax' is the set of axes on which we will plot. There is only 1
# set in this case.
fig, ax = plt.subplots(1,1)

# Set a figure title
fig.suptitle('A plot of the function $f(x) = x^2$', fontsize=14)

# Plot the numbers
ax.plot(x, y)

# Label the x and y axes
ax.set_xlabel('x')
ax.set_ylabel('$x^2$')

# With the line below commented out, the plot will create a
# 'pleasing' look, but the x- and y-axes may be set at a
# different scale. Uncomment the line below to see the
# 'true' aspect ratio of the function.
#ax.set_aspect('equal')

# The x- and y-axes are not displayed by default.
# Uncomment the following lines to display them.
# Full documentation can be read about "spines" here:
# https://matplotlib.org/examples/pylab_examples/spine_placement_demo.html
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# axis label coordinates are not the same as the plotted
# function. They go from 0 to 1, in either direction
# Put the x-label in the center, just below origin
ax.xaxis.set_label_coords(0.5, -0.1) 
# Put the y-label off to the left, centered vertically
ax.yaxis.set_label_coords(0.0, 0.5) 

# Display the plot
plt.show()
