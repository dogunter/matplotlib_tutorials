import numpy as np
import matplotlib.pyplot as plt
 
# Bargraphs are a way of presenting data on various topics.
# the pyplot.bar() plot is described at this URL:
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html
#
# Suppose you took a large poll of students to see how they 
# spend their time throughout a 24 hour day.
# You asked them the following questions:
#    1) How much time to you watch TV (hours)
#    2) How much time to you surf the Internet (hours)?
#    3) How many hours do you sleep per night?
#    4) How much time do you read per day (hours)?
#    5) How much time do you engage in sports/exercise per day (hours)?
#    6) How much time do you work at a job per day (hours)?

# Now define the categories that we will plot, based on the questions
categories = ('Sleep', 'Watch TV', 'Surf Internet', 'Read', 'Sports/Exercise', 'work')

# We will not cover how to process such data, that is, finding the average 
# from all of the answers in each category. Let us assume this is already done.
# For example, suppose the average for each category is the following:
#    sleep: 7.2 hours per day
#       tv: 2.8 hours per day
# Internet: 1.9 hours per day
#     read: 2.3 hours per day
#   active: .78 hours per day
#     work: 5.5 hours per day
#
# Put these into an array of values in the same order as the 'categories' array
averages = [7.2, 2.8, 1.9, 2.3, 0.78, 5.5]

 
# Set up our figure
fig, ax = plt.subplots(1,1,figsize=(10,8))

# The first parameter to the bar() plotting function is the locations along the
# x-axis to put the categories. We will use a simple array of integers from
# 0 to the length of the 'categories' array
x_pos = np.arange(len(categories))

# The second paramter to bar() is the height of the bar to plot. This is our
# 'averages'.
ax.bar(x_pos, averages, align='center', alpha=0.5)

# Instead of xlabels as in previous plots, we have multiple labels, one for each bar.
# Set the tickmarks to be centered, under each bar
ax.set_xticks(x_pos)
# And now display the labels at each tickmark
ax.set_xticklabels(categories)

# Finally, add our title and labels
# The x-axis labels are automatically the names of the first argument passed
# to the bar() plot function.
fig.suptitle('Average time spent by CHS students per day')
ax.set_ylabel('Hours')
 
# At this point we are done, but the reulting plot might make it difficult
# to know the actual value being plotted (2.8 versus 2.9? 2.7?)
# plt.text() allows one to place text anywhere in a plot, so we use this.
# Uncomment the lines below to display each value on top of its bar.
for i, j in enumerate(averages):
    ax.text(x_pos[i] - 0.1, j + 0.05, str(j))

# Explanation
# The enumerate() function adds a counter we can use to step through data.
# for i, j in enumerate(averages) will generate the following values 
# for i and j:
#    0, 7.2
#    1, 2.8
#    2, 1.9
# ... and so on, for the entire list.  This allows us to have 'i' access the
# correct x-position value to place the text. And 'j' can access the correct
# height of the bar, above which we want the text.  We access those values
# but shift the text to the left by adding -0.1 to it. We raise the text
# above the bar by adding 0.05 to the height value.
#

# Show the plot
plt.show()
