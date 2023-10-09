# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(
  x='nb_sold', y='avg_price', kind='scatter', 
  title='Number of avocados sold vs. average price'
)

# Show the plot
plt.show()
