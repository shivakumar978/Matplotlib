import matplotlib.pyplot as plt

# plot style:
plt.style.use('fivethirtyeight') 
# most of these styles have their grid.Therefore, no need to use any grid command at the end again.


days_x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']

# To overlap "Bar-plots" with "Line-plots", simply plot one data in bar and other data as line:

# cost of 100kg Apples in Rupees on the weekdays:
apples_y = [12000, 12050, 13200, 13450, 11200, 14500, 15600]
plt.bar(days_x, apples_y, color='k', label='Apples') # This give Bar-plot

# cost of 100kg Oranges in Rupees on the weekdays:
oranges_y = [9000, 9050, 8200, 8450, 10200, 10500, 11600]
# color 'b'= blue, default linestyle is solid, marker = 'o' = larger marker
plt.plot(days_x, oranges_y, label='Oranges') # This gives a line plot


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
