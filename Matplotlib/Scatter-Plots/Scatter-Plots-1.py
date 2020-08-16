import matplotlib.pyplot as plt

plt.style.use('seaborn')

days_x = [1, 2, 3, 4, 5, 6, 7]
score_y = [10, 25, 32, 15, 21, 12, 15]

# s=size of the value on the map
# c=color
# marker=symbol of the value, however default is a spot
plt.scatter(days_x, score_y, s=100, c='red', edgecolors='black', linewidth=1.5, alpha=0.3) 

plt.show()

