import numpy as np
import matplotlib.pyplot as plt

# plot style:
plt.style.use('fivethirtyeight') 
# most of these styles have their grid.Therefore, no need to use any grid command at the end again.

days_x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']

x_columns = np.arange(len(days_x)) # This creates a variable called x_columns which a array of values.
# These values are numbered version of days_x.

# Now I will create a width for each bar to place them side by side instead of stacking one over the other:
width = 0.20

# Now I need to substract the width from the 1st plotted value and add to last plotted value inoder to have
# the bars side by side. I will not do anything with middle plotted values.

# Also to make the each bar width to be same as the "width" variable, I will add a command 
# before color : "width = width"

# cost of 100kg Apples in Rupees on the weekdays:
apples_y = [12000, 12050, 13200, 13450, 11200, 14500, 15600]
plt.bar(x_columns - width, apples_y, width=width, color='k', label='Apples') # This give Bar-plot

# cost of 100kg Oranges in Rupees on the weekdays:
oranges_y = [9000, 9050, 8200, 8450, 10200, 10500, 11600]
# color 'b'= blue, default linestyle is solid, marker = 'o' = larger marker
plt.bar(x_columns, oranges_y, width=width, label='Oranges') # This gives a line plot

# cost of 100kg Grapes in Rupees on the weekdays:
grapes_y = [6000, 6050, 7200, 7450, 8200, 8500, 9600]
# color 'b'= blue, Linewidth = 3(default=1)
plt.bar(x_columns + width, grapes_y, width=width, label='Grapes')

# Now I need to adjust x axis accordingly:
plt.xticks(ticks=x_columns, labels=days_x) 

# To give labels to the Axis
plt.xlabel('Days')
plt.ylabel('Average cost (Rupees)') 

# To Give Tile to the entire plot
plt.title('Average Cost (Rupees) by Days')

# To know which line belongs to which graph we can add "legend":
# However the labels of the legends are defined in their respective plt.plot(x, y, label='')
plt.legend()

# since my graph was not displaying the names on y-axis and not fitting properly, I used this command:
plt.tight_layout()

plt.show()
