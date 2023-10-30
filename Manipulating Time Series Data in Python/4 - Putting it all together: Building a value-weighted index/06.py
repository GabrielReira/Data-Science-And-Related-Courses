import pandas as pd
import matplotlib.pyplot as plt

components = listings.loc[tickers, ['Market Capitalization', 'Last Sale']]
market_cap_series = stock_prices.mul(no_shares)

# Aggregate and print the market cap per trading day
raw_index = market_cap_series.sum(axis=1)
print(raw_index)

# Normalize the aggregate market cap here 
index = raw_index.div(raw_index.iloc[0]).mul(100)
print(index)

# Plot the index here
index.plot(title='Market-Cap Weighted Index')
plt.show()
