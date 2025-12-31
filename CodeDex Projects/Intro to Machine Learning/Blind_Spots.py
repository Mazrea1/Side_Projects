import pandas as pd

dates = [
  '03/01/2021',
  '17/02/2020',
  '25/03/2019',
  '08/04/2022',
  '14/05/2018',
  '29/06/2023',
  '10/07/2020',
  '22/08/2021',
  '05/09/2017',
  '31/10/2024'
]

df = pd.DataFrame({'date': dates})

# Extract the month using string slicing
df['month'] = df['date'].str[3:5]
# Extract the year using string slicing
df['year'] = df['date'].str[6:10]

print(df['month'])
print(df['year'])