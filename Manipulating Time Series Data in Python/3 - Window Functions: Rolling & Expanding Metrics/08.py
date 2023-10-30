import pandas as pd
from numpy.random import choice, seed
import seaborn as sns
import matplotlib.pyplot as plt

# Import data here
fb = pd.read_csv('facebook_stock_price.csv')

# Set seed here
seed(42)

# Calculate daily_returns here
daily_returns = fb.pct_change().dropna()

# Get n_obs
n_obs = daily_returns.count()

# Create random_walk
random_walk = choice(daily_returns, size=n_obs)

# Convert random_walk to pd.series
random_walk = pd.Series(random_walk)

# Plot random_walk distribution
sns.distplot()
plt.show()
