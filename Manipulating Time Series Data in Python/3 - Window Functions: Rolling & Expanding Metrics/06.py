import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import data here
data = pd.read_csv('GOOG_AAPL.csv')

# Define a multi_period_return function
def multi_period_return(period_returns):
  return np.prod(period_returns + 1) - 1
    
# Calculate daily returns
daily_returns = data.pct_change()

# Calculate rolling_annual_returns
rolling_annual_returns = daily_returns.rolling('360D').apply(multi_period_return)

# Plot rolling_annual_returns
rolling_annual_returns.mul(100).plot()
plt.show()
