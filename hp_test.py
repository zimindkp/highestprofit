# K Parekh
# Oct 8 2021
# Github Challenge - SADA
# Highest Profit

import pandas as pd
import urllib.request
import numpy as np

# PART 1
# Setting url for file download as "raw"
url = 'https://gist.github.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv'
response = urllib.request.urlopen(url)

# Read this url into memory as a csv dataframe
data = pd.read_csv(response)
data3 = response.read()

# Count number of rows - adding 1 to account for the first row as a header
print('Number of rows in file are: ', len(data)+1)

# Purging non-numeric values for profit
# Used another function to get number of rows here
data= data[pd.to_numeric(data['Profit (in millions)'], errors='coerce').notnull()]
print("\nNumber of rows after purging non-numeric values for profit are: ", data.shape[0]+1)

# PART 2
# Convert numbers to signed
data["Profit (in millions)"] = pd.to_numeric(data["Profit (in millions)"], downcast="signed")

# Write to a JSON file with
with open('data2.json', 'w', encoding='utf-8') as f:
    f.write(data.to_json(orient='records', lines=True))

# Sorting the data by Profit (ascending order)
data.sort_values(by='Profit (in millions)', inplace=True)

# Output of the top 20 values
print("\nTop 20 rows with the highest profit values:")
print(data.iloc[::-1].head(20))


