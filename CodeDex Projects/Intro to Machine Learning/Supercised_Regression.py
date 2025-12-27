import pandas as pd
from sklearn.linear_model import LinearRegression

# Creating the dataset
data = pd.DataFrame({
  'size_sqft': [450, 500, 600, 750, 800, 850, 900, 1000, 1100, 1200],
  'floor':     [1, 2, 1, 3, 5, 4, 2, 6, 7, 10],
  'bedrooms':  [1, 1, 1, 2, 2, 2, 2, 3, 3, 3],
  'price':     [1200, 1300, 1450, 1600, 1700, 1750, 1800, 2000, 2150, 2300]
})

# Splitting the dataset into X and y
X = data[['size_sqft', 'floor', 'bedrooms']]
y = data['price']

# Example: 950 sqft, 5th floor, 2 bedrooms
new_apartment = pd.DataFrame({
  'size_sqft': [950],
  'floor': [5],
  'bedrooms': [2]
})

my_model = LinearRegression()
my_model.fit(X, y)
predictions = my_model.predict(new_apartment)
print(predictions)