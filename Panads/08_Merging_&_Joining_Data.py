import pandas as pd
 
employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DeptID": [10, 20, 30]
})

print(employees,"\n")

departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "DeptName": ["HR", "Engineering", "Marketing"]
})

print(departments,"\n")

# Join 

#Inner join 
print("\n Inner Join \n")

df = pd.merge(employees , departments , on="DeptID")
print(df)

# Outer join 
print("\n Outer join \n")

df1 = pd.merge(employees , departments , on="DeptID", how="outer")
print(df1)

# Right and Left Join
print("\n Right amd Left Join \n")

df2 = pd.merge(employees , departments , on="DeptID", how="right")
print(df2,"\n")

df4 = pd.merge(employees , departments , on="DeptID", how="left")
print(df4)

# Concatenating DataFrame
print("\n Concatenating DataFrame \n")

df5 = pd.DataFrame({"Name": ["Alice", "Bob"]})
df6 = pd.DataFrame({"Name": ["Charlie", "David"]})

print(df5, "\n")
print(df6, "\n")

df7 = pd.concat([df5,df6])
print(df7)

df8 = pd.DataFrame({"ID": [1, 2]})
df9 = pd.DataFrame({"Score": [90, 80]})

df0 = pd.concat([df8, df9], axis=1)
print(df0)