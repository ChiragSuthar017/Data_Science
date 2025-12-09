import pandas as pd

# import csv file 
data = pd.read_csv(r"D:\Data Science\Data_Science\Panads\data1.csv")
print(data)

# selecting columns
print("\n selecting columns")
print(data["Actor"]) # select single columns
print(data[["Actor","IMDb"]])  # select multiple columns

# selecting rows
print("\n selecting rows")
print(data.loc[1]) # select rows by label
print(data.iloc[1]) # select rows by index 

# select specific rows and columns
print("\n select specific rows and columns")
print(data.loc[0 , "Actor"]) # selete by label
print(data.iloc[0,0]) # select by index

# select specific rows and columns in range
print("\n select specific rows and columns in range")
print(data.loc[0:2,["Actor","IMDb"]])
print(data.iloc[0:2,0:3])

# fast access (These are optimized for single element access)
print("\n fast access (These are optimized for single element access)")
print(data.at[0,"Actor"]) # select by label
print(data.iat[0,1]) # select by index

# Filtering with Conditions
print("\n Filtering with Conditions")

# Simple Condition
print("Simple Condition")
print(data[data["IMDb"]>6]) # Only give rows that are greater than IMDb 6

# Multiple Conditions (AND / OR)
print("\n Multiple Conditions (AND / OR)")
print("\n And operator")
print(data[(data["IMDb"]>6) & (data["Year"]>2016)]) # And operator
print("\n Or operator")
print(data[(data["IMDb"]>6) | (data["Year"]>2016)]) # Or operator

# Querying with .query()
print("\n Querying with .query()")

# The .query() method in pandas lets you filter DataFrame rows using a string expression — it's a more readable and often more concise alternative to using boolean indexing
# .query() returns a copy, not a view
print(data.query("IMDb > 6 and Year > 2016"))

# we can create a copy
print("\n we can create a copy")

data1 = data[["Actor","IMDb"]].copy() # its nor affect our original data , data1 is a copy of data
print(data1)