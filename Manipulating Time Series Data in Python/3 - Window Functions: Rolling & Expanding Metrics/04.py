import pandas as pd
import matplotlib.pyplot as plt

# Import data here
data = pd.read_csv('google_stock_prices.csv')

# Calculate differences
differences = data.diff().dropna()

# Select start price
start_price = data.first('D')

# Calculate cumulative sum
cumulative_sum = start_price.append(differences).cumsum()

# Validate cumulative sum equals data
print(data.equals(cumulative_sum))
