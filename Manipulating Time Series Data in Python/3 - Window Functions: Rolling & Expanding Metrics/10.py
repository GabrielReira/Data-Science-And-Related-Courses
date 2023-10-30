import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import data here
data = pd.read_csv('AAPL_AMZN_IBM_WMT_XOM.csv')

# Inspect data here
print(data.info())

# Calculate year-end prices here
annual_prices = data.resample('A').last()

# Calculate annual returns here
annual_returns = annual_prices.pct_change()

# Calculate and print the correlation matrix here
correlations = annual_returns.corr()
print(print(correlations))

# Visualize the correlations as heatmap here
sns.heatmap(correlations, annot=True)
plt.show()
