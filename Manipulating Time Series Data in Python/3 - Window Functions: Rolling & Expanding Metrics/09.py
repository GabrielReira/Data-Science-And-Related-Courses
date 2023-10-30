import pandas as pd
from numpy.random import choice, seed
import matplotlib.pyplot as plt

# Import data here
fb = pd.read_csv('facebook_stock_price.csv')
random_walk

# Select fb start price here
start = fb.price.first('D')

# Add 1 to random walk and append to start
random_walk = random_walk.add(1)
random_price = start.append(random_walk)

# Calculate cumulative product here
random_price = random_price.cumprod()

# Insert into fb and plot
fb['random'] = random_price
fb.plot()
plt.show()
