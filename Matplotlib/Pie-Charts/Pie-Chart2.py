import matplotlib.pyplot as plt

# plot style:
plt.style.use('fivethirtyeight')

slices = [7000, 8000, 9250, 6750, 8087]
labels = ['Apples', 'Oranges', 'Grapes', 'Bananas', 'strawberries']

# To emphasize on a paticular label I used "explode" argument:
explode = [0, 0, 0.1, 0, 0] # to explode 3rd item on labels list

# To add a shadow to the pie chart that makes it look like 2D graph, I passed the argument "shadow=True":
# To rotate the chart, I use the argument "startangle":
# To display the percentage of the slices, I used the arguement "autopct='%1.1f%%' "
plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=60, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("Simple Pie Chart")
plt.tight_layout()
plt.show()