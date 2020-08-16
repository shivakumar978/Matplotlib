import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn') # we can use any style like 'ggplot', 'fivethirtyeight', etc...here I used 'seaborn'

data = pd.read_csv('Data.csv')
days = data['Days']
apples = data['Apples']
oranges = data['Oranges']
grapes = data['Grapes']

# to get plots on 2 different figures instead of same plot:

fig1, (ax1) = plt.subplots()
fig2, (ax2) = plt.subplots()

ax1.plot(days, apples, label='Apples')
ax2.plot(days, oranges, label='Oranges')
ax2.plot(days, grapes, color='y', linestyle='--', label='Grapes')

ax1.legend()
ax1.set_title('Average Cost (Rupees) by Days')
ax1.set_ylabel('Average cost (Rupees)') 

ax2.legend()
ax2.set_xlabel('Days')
ax2.set_ylabel('Average cost (Rupees)') 

plt.tight_layout()

plt.show()