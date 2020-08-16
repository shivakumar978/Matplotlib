import pandas as pandas
import matplotlib.pyplot as plt

days_x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']

# cost of 100kg Apples in Rupees on the weekdays:
apples_y = [12000, 12050, 13200, 13450, 11200, 14500, 15600]
plt.plot(days_x, apples_y, color='k', linestyle='--', marker='.', label='Apples')

# cost of 100kg Oranges in Rupees on the weekdays:
oranges_y = [9000, 9050, 8200, 8450, 10200, 10500, 11600]
plt.plot(days_x, oranges_y, label='Oranges')

# cost of 100kg Grapes in Rupees on the weekdays:
grapes_y = [6000, 6050, 7200, 7450, 8200, 8500, 9600]
plt.plot(days_x, grapes_y, label='Grapes')

# to fill the Area:
plt.fill_between(days_x, oranges_y, alpha=0.30) # alpha allows you to see throw the Area filled

# To give labels to the Axis
plt.xlabel('Days')
plt.ylabel('Average cost (Rupees)') 

# To Give Tile to the entire plot
plt.title('Average Cost (Rupees) by Days')


plt.legend()
plt.tight_layout()
plt.show()
