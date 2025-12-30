import pandas as pd
from sklearn.cluster import KMeans

data = {
  'City': [
    'Seattle', 'Boston', 'San Francisco', 'Chicago', 'Minneapolis',
    'Denver', 'Miami', 'Houston', 'Phoenix', 'Las Vegas'
  ],
  'Average Temperature': [
    60, 63, 68, 65, 55,
    70, 85, 88, 90, 95
  ],
  'Average Humidity': [
    80, 70, 75, 60, 50,
    40, 85, 90, 20, 15
  ]
}

df = pd.DataFrame(data)

# Select the features for clustering
X = df[['Average Temperature', 'Average Humidity']]

# A new datapoint that we'll cluster after making the model
new_city = [[85, 40]]  # Format must be a 2D list or array

model = KMeans(n_clusters=3, random_state=42)
model.fit(X)
new_city_cluster = model.predict(new_city)
print(new_city_cluster)