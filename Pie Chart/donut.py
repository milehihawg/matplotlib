"""
===============
Basic pie chart
===============

Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['White (87.5%)', 'Black/African American(4.5%)', 'American Indian (1.6%)', 'Asian (3.3%)', 'Two or More Races (3.0%)']
sizes = [87.5, 4.5, 1.6, 3.3, 3.0]
explode = (0, .25, .25, .25, .25)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, 
        shadow=False, startangle=25)
#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.25,color='black', fc='white',linewidth=1.0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
