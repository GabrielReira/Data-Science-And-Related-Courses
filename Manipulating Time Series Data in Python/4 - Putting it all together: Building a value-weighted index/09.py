import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

index = pd.Series()
data = pd.read_csv('dow_jones_industrial_average.csv')

# Inspect data
print(data.info())
print(data.head(5))

# Create multi_period_return function here
def multi_period_return(r):
  return (np.prod(r + 1) - 1) * 100

# Calculate rolling_return_360
rolling_return_360 = data.pct_change().rolling('360D').apply(multi_period_return)

# Plot rolling_return_360 here
rolling_return_360.plot(title='Rolling 360D Return')
plt.show()
