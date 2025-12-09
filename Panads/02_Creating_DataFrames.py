# creating data frame 
import pandas as pd

# create data frame with dictionary 
a = {
    "name" : ["chirag" , "prince", "bhavy"],
    "age"  : [20,21,19],
    "city" : ["rajasthan", "delhi", "gujarat"] 
}
a1 = pd.DataFrame(a)
print(a1)

# create data frame with list
print("\n create data frame with list")
b = [["chirag", 90],["mehul",88],["rohan",85]]
b1 = pd.DataFrame(b, columns=["name","marks"])
print(b1)

# create data frame with numpy
print("\n create data frame with dictionary ") 
import numpy as np
arr = np.array([[1,2],[3,4]])
arr1 = pd.DataFrame(arr,columns=["A","B"])
print(arr1)

# Read excel file using pandas
print("\n Read excel file using panads")
print(".xlsx file")
c = pd.read_excel(r"D:\Data_Science\Panads\data.xlsx")
print(c)

print("\n .csv file")
d = pd.read_csv(r"D:\Data_Science\Panads\data.csv")
print(d)

# Read json file using pandas
print("\n Read json file ")
e = pd.read_json(r"D:\Data_Science\Panads\data.json")
print(e)

# Read csv file using url 
print("\n Read csv file using url/link")
f = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
print(f)

# EDA (Exploratory Data Analysis)
print("\n EDA (Exploratory Data Analysis)")
print(" \n First five rows")
print(f.head()) # first five rows
print(" \n last five rows")
print(f.tail()) # last five rows
print(" \n Column info: types, non-nulls")
print(f.info()) # Column info: types, non-nulls
print(" \n state for the numeric columns")
print(f.describe()) # state for the numeric columns
print(" \n list columns names")
print(f.columns) # list columns names
print("\n rows, columns")
print(f.shape) # rows, columns