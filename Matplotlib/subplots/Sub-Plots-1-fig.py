import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn') # we can use any style like 'ggplot', 'fivethirtyeight', etc...here I used 'seaborn'

data = pd.read_csv('Data.csv')
days = data['Days']
apples = data['Apples']
oranges = data['Oranges']
grapes = data['Grapes']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

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