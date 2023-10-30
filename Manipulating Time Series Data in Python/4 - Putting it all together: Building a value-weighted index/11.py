import pandas as pd

stock_prices = pd.read_csv('stock_prices.csv')
index = pd.Series()

# Inspect index and stock_prices
print(index.info())
print(stock_prices.info())

# Join index to stock_prices, and inspect the result
data = stock_prices.join(index)
print(data.info())

# Create index & stock price returns
returns = data.pct_change()

# Export data and data as returns to excel
with pd.ExcelWriter('data.xls') as writer:
  data.to_excel(excel_writer=writer, sheet_name='data')
  returns.to_excel(excel_writer=writer, sheet_name='returns')
