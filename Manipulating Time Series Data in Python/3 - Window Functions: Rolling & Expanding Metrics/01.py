import pandas as pd
import matplotlib.pyplot as plt

# Import and inspect ozone data here
data = pd.read_csv('ozone.csv', parse_dates=['date'], index_col='date')
print(data.info())

# Calculate 90d and 360d rolling mean for the last price
data['90D'] = data['Ozone'].rolling(window='90D').mean()
data['360D'] = data['Ozone'].rolling(window='360D').mean()

# Plot data
data.loc['2010':].plot(title='New York City')
plt.show()
