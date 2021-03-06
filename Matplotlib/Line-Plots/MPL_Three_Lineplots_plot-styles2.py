import matplotlib.pyplot as plt

# To get the comic version graph we can use a 'Method' called "xkcd":
plt.xkcd()


days_x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']

# cost of 100kg Apples in Rupees on the weekdays:
apples_y = [12000, 12050, 13200, 13450, 11200, 14500, 15600]
# To add 'color', 'linestyle', 'markers' to the plotted line: k=black, -- = dottedline, marker='.'=1
plt.plot(days_x, apples_y, color='k', linestyle='--', marker='.', label='Apples')

# cost of 100kg Oranges in Rupees on the weekdays:
oranges_y = [9000, 9050, 8200, 8450, 10200, 10500, 11600]
# color 'b'= blue, default linestyle is solid, marker = 'o' = larger marker
plt.plot(days_x, oranges_y, label='Oranges')

# cost of 100kg Grapes in Rupees on the weekdays:
grapes_y = [6000, 6050, 7200, 7450, 8200, 8500, 9600]
# color 'b'= blue, Linewidth = 3(default=1)
plt.plot(days_x, grapes_y, label='Grapes')


# To give labels to the Axis
plt.xlabel('Days')
plt.ylabel('Average cost (Rupees)') 

# To Give Tile to the entire plot
plt.title('Average Cost (Rupees) by Days')

# To know which line belongs to which graph we can add "legend":
# However the labels of the legends are defined in their respective plt.plot(x, y, label='')
plt.legend()

# since my graph was not displaying the names on y-axis and not fitting properly, i used this command:
plt.tight_layout()

plt.show()