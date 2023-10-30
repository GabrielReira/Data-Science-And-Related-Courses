import pandas as pd
import matplotlib.pyplot as plt

components = listings.loc[tickers, ['Market Capitalization', 'Last Sale']]
stock_prices = pd.read_csv('stock_prices.csv', parse_dates=['Date'], index_col='Date')

# Select the number of shares
no_shares = components['Number of Shares']
print(no_shares.sort_values())

# Create the series of market cap per ticker
market_cap = stock_prices.mul(no_shares)

# Select first and last market cap here
first_value = market_cap.iloc[0]
last_value = market_cap.iloc[-1]

# Concatenate and plot first and last market cap here
pd.concat([first_value, last_value], axis=1).plot(kind='barh')
plt.show()
