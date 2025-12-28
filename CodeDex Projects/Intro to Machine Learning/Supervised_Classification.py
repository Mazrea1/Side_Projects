import pandas as pd
import sklearn.datasets
import sklearn.neighbors

# Gets the data from sklearn
data = sklearn.datasets.load_breast_cancer()

# Loads the data into a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Getting the first 500 tumors and splitting the data into features and target
X = df.drop(columns='target').iloc[:500]
y = df['target'].iloc[:500]

my_model = sklearn.neighbors.KNeighborsClassifier()
my_model.fit(X, y)

row_501 = df.drop(columns='target').iloc[[500]]
prediction = my_model.predict(row_501)
print(prediction)