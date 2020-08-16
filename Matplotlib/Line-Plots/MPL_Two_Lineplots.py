
import matplotlib.pyplot as plt


days_x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']

# cost of 100kg Apples in Rupees on the weekdays:
apples_y = [12000, 12050, 13200, 13450, 11200, 14500, 15600]
plt.plot(days_x, apples_y, label='Apples')

# cost of 100kg Oranges in Rupees on the weekdays:
oranges_y = [9000, 9050, 8200, 8450, 10200, 10500, 11600]
plt.plot(days_x, oranges_y, label='Oranges')

# To give labels to the Axis
plt.xlabel('Days')
plt.ylabel('Average cost (Rupees)') 

# To Give Tile to the entire plot
plt.title('Average Cost (Rupees) by Days')

# To know which line belongs to which graph we can add "legend":
# However the labels of the legends are defined in their respective plt.plot(x, y, label='')
plt.legend()

plt.show()