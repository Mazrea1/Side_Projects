import pandas as pd

# Popular mobile apps
app_data = {
  'app_name': [
    'YouTube', 'TikTok', 'Instagram', 'Spotify', 'Duolingo',
    'Twitter', 'Headspace', 'Discord', 'Depop'
  ],
  'category': [
    'Video', 'Social Media', 'Social Media', 'Music', 'Education',
    'Social Media', 'Health', 'Communication', 'Shopping'
  ],
  'rating': [
    4.7, 4.6, 4.5, 4.6, 4.7,
    4.3, None, 4.7, 4.4
  ],
  'downloads_millions': [
    5000, 3000, 3500, 2000, None,
    1500, 500, 600, 200
  ]
}

# Create the DataFrame
apps = pd.DataFrame(app_data)
print(apps.head()) #First 5 rows
print(apps.tail()) #Last 5 rows
print(apps.info()) #Shows data in a more specific way including missing data
print(apps.describe(include='all')) #Shows the mean, min, max, standard deviation, include='all' add non-numerical columns



