"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars.
"""
import numpy as np
import matplotlib.pyplot as plt


NewYork_means = (36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48)

ind = np.arange(len(NewYork_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

rects2 = ax.bar(ind + width/2, NewYork_means, width, yerr=0,
                color='red', label='NewYork')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temperature (F)')
ax.set_title('Monthly Temperatures in New York')
ax.set_xticks(ind)
ax.set_xticklabels(('J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'))
ax.legend()

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects2, "center")

plt.show()
