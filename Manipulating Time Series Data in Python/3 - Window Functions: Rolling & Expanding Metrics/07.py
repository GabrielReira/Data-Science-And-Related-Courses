import pandas as pd
from numpy.random import normal, seed
import matplotlib.pyplot as plt

# Set seed here
seed(42)

# Create random_walk
random_walk = normal(loc=.001, scale=.01, size=2500)

# Convert random_walk to pd.series
random_walk = pd.Series(random_walk)

# Create random_prices
random_prices = random_walk.add(1).cumprod()

# Plot random_prices here
random_prices.mul(1000).plot()
plt.show()
