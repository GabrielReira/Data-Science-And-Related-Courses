import pandas as pd
import matplotlib.pyplot as plt

components = listings.loc[tickers, ['Market Capitalization', 'Last Sale']]
index = raw_index.div(raw_index.iloc[0]).mul(100)

# Calculate and print the index return here
index_return = (index.iloc[-1]/index.iloc[0]-1)*100
print(index_return)

# Select the market capitalization
market_cap = components['Market Capitalization']

# Calculate the total market cap
total_market_cap = market_cap.sum()

# Calculate the component weights, and print the result
weights = market_cap.div(total_market_cap)
print(weights.sort_values())

# Calculate and plot the contribution by component
weights.mul(index_return).sort_values().plot(kind='barh')
plt.show()
