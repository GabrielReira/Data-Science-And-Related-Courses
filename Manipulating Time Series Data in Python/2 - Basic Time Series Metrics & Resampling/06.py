import pandas as pd
import matplotlib.pyplot as plt

# Import data here
monthly = pd.read_csv('unemployment.csv', parse_dates=['date'], index_col='date')

# Inspect data here
print(monthly.info())

# Create weekly dates
weekly_dates = pd.date_range(
  start=monthly.index.min(),
  end=monthly.index.max(),
  freq='W'
)

# Reindex monthly to weekly data
weekly = monthly.reindex(weekly_dates)

# Create ffill and interpolated columns
weekly['ffill'] = weekly.UNRATE.ffill()
weekly['interpolated'] = weekly.UNRATE.interpolate()

# Plot weekly
weekly.plot()
plt.show()
