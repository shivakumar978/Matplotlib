
import matplotlib.pyplot as plt


days_x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']

# cost of 100kg Apples in Rupees on the weekdays:
apples_y = [12000, 12050, 13200, 13450, 11200, 14500, 15600]

plt.plot(days_x, apples_y)

# To give labels to the Axis
plt.xlabel('Days')
plt.ylabel('Average cost (Rupees)') 

# To Give Tile to the entire plot
plt.title('Average Cost (Rupees) by Days')

plt.show()