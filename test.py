# K Parekh
# Github Challenge - SADA
# Highest Profit

# import csv reader library
import csv
import pandas as pd

file = open('data.csv')
print (type(file))

csvreader=csv.reader(file)

header = []
header = next(csvreader)
header
print(header)
rows=len(list(csvreader))
print('Number of rows in file are ', rows )
print('hello')
file.close()


