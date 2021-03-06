import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

days_x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturday', 'sunday']


plt.hist(days_x, bins=5, edgecolor='black') # bins divide your data groups. I have 7 days divided into 5 bins

plt.xlabel('Days')
plt.ylabel('Average cost (Rupees)') 

plt.title('Average Cost (Rupees) by Days')

plt.legend()

plt.tight_layout()

plt.show()