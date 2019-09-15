# [What does each visual represent](#home)

Creating visuals is a good way to show what your data says in an easy to understand format.

When creating visuals for our data, it is important to know where the data came from, how it is important, and why we used a specific visual. 


# [Price vs Year Built](#price-vs-year)

This visualization explores the relationship between price and the age of the house.

![Price per year](/pricevyear.png)

The graph is a histogram, with the x-axis as age and the y-axis as price.

Although it is not a clear line, as age increases, the price generally decreases.

# [Ratio of beds and baths vs price](#bed-baths-vs-price)

This visualization explores the relationship between price and the how many beds and baths are in the hoe.

![Beds and baths vs price](/bedsbathsvsprice.png)

The graph is a histogram, with the x-axis as the percentage of beds and baths and the y-axis as price.

The "bell-curve" of the graph is skewed left, with the most expensive homes having 2 times more beds than bathrooms.

# [Average price based on number of beds](#beds-vs-price)

This visualization explores the relationship between price and number of beds.

![Price per bed](/bedsvsprice.png)

The graph is a histogram, with the x-axis as number of beds and the y-axis as price.

This graph shows a nice bell curve, with the highest price correlated to 7 beds.

# [All Prices](#prices)

This visualization explores the distrubution of housing prices across our dataset.

![All Prices](/allprices.png)

The graph is a histogram, with the x-axis as price and the y-axis as total count.

This shows that most of our homes are under $1 million, with the vast majority being around $500K.

# [Average price per city](#price-per-city)

This visualization explores the relationship between price and the city where the house is located.

![Price per city](/cityvsprice.png)

The x-axis is a bit busy because this source code is meant to be modified. The user should change the code in different ways, such as sorting by price or sorting by City name to see how the graph changes.

The graph is a histogram, with the x-axis as city and the y-axis as price.

This histogram shows that the most expensive city is Raleigh, and the other homes have an average price of around $500K

# [Distribution of homes, with gradient of price](#home-location-vs-price)

This visualization explores the relationship between the location of the house (latitude by longitude) and the price of the house.

![Price gradient](/gradient.png)

The graph is a scatterplot, with the x-axis as latitude and the y-axis as longitude. There is another dimension added, color, which displays how much each home costs. Blue represents lowest prices, while red represents highest.

This shows that most of the more expensive homes are centrally located, with some in the south, while the less expensive homes are on the outer edges of the map.
