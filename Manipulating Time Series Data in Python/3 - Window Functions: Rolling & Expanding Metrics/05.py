import pandas as pd
import matplotlib.pyplot as plt

# Import data here
data = pd.read_csv('google_apple_stock_prices.csv')

# Define your investment
investment = 1000

# Calculate the daily returns here
returns = data.pct_change()

# Calculate the cumulative returns here
returns_plus_one = returns.add(1)
cumulative_return = returns_plus_one.cumprod()

# Calculate and plot the investment return here 
(cumulative_return.mul(investment)).plot()
plt.show()
