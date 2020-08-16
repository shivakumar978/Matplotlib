
import matplotlib.pyplot as plt

# plot style:
plt.style.use('fivethirtyeight') 

slices = [160, 40, 90, 35]
labels = ['One Hundred Sixty', 'Forty', 'Chocolate', 'Almonds']

# I used wedgeprops for marking the edges. Its a dict of "key:value pair"
plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})

plt.title("Simple Pie Chart")

plt.tight_layout()
plt.show()