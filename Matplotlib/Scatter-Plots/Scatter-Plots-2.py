import matplotlib.pyplot as plt

plt.style.use('seaborn')

days_x = [1, 2, 3, 4, 5, 6, 7]
score_y = [10, 25, 32, 15, 21, 12, 15]

# To give each point a differnt color: and later use the "cmap='Reds"
colors = [3, 5, 9, 4, 2, 6, 1]

#If I have different size of data:
sizes = [300, 450, 500, 250, 150, 200, 350]

# s=size of the value on the map
# c=color
# marker=symbol of the value, however default is a spot
plt.scatter(days_x, score_y, s=sizes, c=colors, cmap='Reds', edgecolors='black', linewidth=1.5, alpha=0.3) 

#label for color map: That is the intensity of the color 
cbar = plt.colorbar()

#To set a lab:
cbar.set_label('Test Score')

plt.show()
