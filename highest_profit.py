# K Parekh
# Oct 10 2021
# Github Challenge - SADA
# Highest Profit

import pandas as pd
import numpy as np
import json

# read file into memory as a Pandas Dataframe
file_read = pd.read_csv('data.csv')
print('Number of rows in file are: ', file_read.shape[0])

#print("Purging non-numeric values for profit....")
file_read= file_read[pd.to_numeric(file_read['Profit (in millions)'], errors='coerce').notnull()]
print("\nNumber of rows after purging non-numeric values for profit are: ", file_read.shape[0])

# Convert numbers to signed
file_read["Profit (in millions)"] = pd.to_numeric(file_read["Profit (in millions)"], downcast="signed")
with open('data2.json', 'w', encoding='utf-8') as f:
    f.write(file_read.to_json(orient='records', lines=True))

# Sorting the data by Profit (ascending order)
file_read.sort_values(by='Profit (in millions)', inplace=True)

# Output of the top 20 values
print("\nTop 20 rows with the highest profit values:")
print(file_read.iloc[::-1].head(20))


