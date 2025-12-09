import pandas as pd

a = pd.read_csv(r"D:\Data_Science\Panads\data1.csv")
print(a)

# Sorting & ranking

#Sort by values
print("\n Sort by values \n")
print(a.sort_values("Year"),"\n") # give ascending order
print(a.sort_values("Year", ascending=False)) # give descending order
print(a.sort_values(["Year"  , "IMDb"])) # if year are same then sort according to IMDb

b = a.sort_values(["Year" , "IMDb"]).copy()

# reset index
print("\n Reset index \n")
print(b.reset_index()) # give me a new data frame with index come as ascending order and give a new index column its not change my old data
print(b.reset_index(drop=True)) # its give a new index but drop old index 
print(b)
b.reset_index(drop=True, inplace=True) # its chhange my old data 
print(b)

# sort by index
print("\n Sort by Index \n")
c = a.sort_values(["Year","IMDb"]).copy()
print(c)
print(c.sort_index()) # sort by index

# sort by Ranking 
print("\n Sort by Ranking \n")
c["Rank"]=c["IMDb"].rank() # bigger IMDb score give bigger rank also give average of rank for same IMDb score
print(c)
c["Rank"]=c["IMDb"].rank(ascending=False) # give rank 1 of the bigger score
print(c)
c["Rank"]=c["IMDb"].rank(ascending=False, method="dense") # give same rank for same IMDb score
print(c)

# Renaming Columns & Index
print(" \n Renaming Columns & Index \n")

print(c.rename(columns={"Actor" : "Actors"})) # change the name colmns name and give a copy of data
c.rename(columns={"Actor" : "Actors"},inplace=True) # chnage the original data
print(c)

# c.columns = ["Name", "Age", "City"] # for rename all columns

# c.rename(index={0:"row1",1:"row2"}) # change index 

# Changing Column Order
print("\n Changing Column Order \n")

c = c[["Film","Actors","Year","Genre","IMDb","BoxOffice(INR Crore)"]] # change the columns order
print(c)

d = ["IMDb"] + [d for d in c.columns if d != "IMDb"] # move only one columns in front 
c = c[d]
print(c[d])