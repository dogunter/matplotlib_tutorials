import numpy as np
import matplotlib.pyplot as plt

# A continuation of 1-simple_plot.py to show that
# multiple functions can be plotted on the same
# axes.

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
y1 = x*x

# Another function to plot: y = x^3
y2 = x*x*x

# Set up the plot
# plt.subplots() lets us create multiple plots in a figure if we wish.
# The arguments specify the number of rows and columns. We only need 1.
# 'fig' is the overall figure in which we will plot.
# 'ax' is the set of axes on which we will plot. There is only 1
# set in this case.
fig, ax = plt.subplots(1,1)

# Set a figure title
fig.suptitle('A plot of the functions $f(x) = x^2$ and $f(x) = x^3$', fontsize=14)

# Plot the numbers
# The first plot will be blue, the second will be red.
# Now that we have two plots, we should include a legend
# for the reader to know which is which
ax.plot(x, y1, 'b', label='$x^2$')
ax.plot(x, y2, 'r', label='$x^3$')
ax.legend()

# Label the x and y axes
ax.set_xlabel('x')
ax.set_ylabel('$f(x)$')

# With the line below commented out, the plot will create a
# 'pleasing' look, but the x- and y-axes may be set at a
# different scale. Uncomment the line below to see the
# 'true' aspect ratio of the function.
#ax.set_aspect('equal')

# The x- and y-axes are not displayed by default.
# Uncomment the following lines to display them.
# Full documentation can be read about "spines" here:
# https://matplotlib.org/examples/pylab_examples/spine_placement_demo.html
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
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

# Notice that the automatic limits of the plot are larger in the
# y-direction. This is will make the x^2 plot look squished.
# Uncomment the line below to set plot limits for the y-axis
ax.set_ylim(-20,20)

# Display the plot
plt.show()

