import pandas as pd
# import csv file as data
data = pd.read_csv(r"D:\Data_Science\Panads\data_cleaning_sample.csv")
print(data)

# Handling Missing values
print("\n Handling Missing values")
print(data.isnull())  # give true for NaNs values
print(data.isnull().sum()) # count missing values per columns 

# Drop Missing data
print("\n Drop Missing data") 
print(data.dropna()) # Drop row with any missing values
print(data.dropna(axis=1)) # Drop columns with missing values

# Fill missing values
print("\n Fill missing values")
print(data.fillna(0)) # Fill missing values into 0
print(data["Age"].fillna(data["Age"].mean())) # replace missing value into mean
print(data.ffill()) # forward fill
print(data.bfill()) # backward fill\

# Detecting and Removing Dulplicates
print("\n Detecting and Removing Dulplicates")
print(data.duplicated()) # give true for duplicates
print(data.drop_duplicates()) # drop duplicate rows
print(data.duplicated(subset=["Name","Age"])) # give true for duplicates on specific columns

# String operations with .str
print("\n String operations with .str \n")
print(data["Name"].str.lower())
print(data["City"].str.contains("delhi", case= False)) # check if delhi is in the city name case insensitive(give true if city = delhi)
print(data["Email"].str.split("@")) # Outputs a pandas Series where each element is a list of strings (the split parts). This is where a Python list comes into play, but the outer object is still a pandas Series.

# Copy data and Remove duplicates
print("\n Copy data and Remove duplicates \n")
data1 = data.dropna().copy()
print(data1)

#  Type Conversions with .astype()
print("\n Type Conversions with .astype() \n")
print(data1["Age"].astype(int)) # convert data type float to int
data["Join Date"] = pd.to_datetime(data["Join Date"], errors='coerce')
print(data)     

# Applying Functions
print("\n Applying Functions \n")

# .apply() Apply any function to rows or columns
print(".apply() \n")
data1["Age Group"] = data1["Age"].apply(lambda x : "Adult" if x >= 18 else "Minor") # apply any type of function
print(data1) 

# .map() Element wise mapping for series
print("\n .map() \n")
gender_map = {"M": "Male", "F": "Femail", "O": "Other"}
data1["Gender"] = data1["Gender"].map(gender_map) # replace all values in Gender
print(data1)

# .replace() replace spacific values
print("\n .replace() \n") # replace specific values
data1["City"] = data1["City"].replace({"Delhi": "New Delhi" , "Mumbai": "New Mumbai"})
print(data1)