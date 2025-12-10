import pandas as pd
df = pd.DataFrame({
    "Department": ["HR", "HR", "IT", "IT", "Marketing", "Marketing", "Sales", "Sales"],
    "Team": ["A", "A", "B", "B", "C", "C", "D", "D"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Salary": [85, 90, 78, 85, 92, 88, 75, 80],
    "Age": [23, 25, 30, 22, 28, 26, 21, 27],
    "JoinDate": pd.to_datetime([
        "2020-01-10", "2020-02-15", "2021-03-20", "2021-04-10",
        "2020-05-30", "2020-06-25", "2021-07-15", "2021-08-01"
    ])
})  
print(df)


# .groupby()
print("\n .groupby() \n")

df1 = df.groupby(["Team","Department"])["Salary"].mean().reset_index(name="avg salary")
print(df1)

# .aggregate() / .agg()  ## both are same
print("\n .agg() \n")

df2 = df.groupby("Team")["Salary"].agg(["mean","sum","min","max"])
print(df2)

# .transform()
print("\n  .transform() \n")
df3 = df
df3["Team Avg"] = df.groupby("Team")["Salary"].transform("mean")
print(df3)

# .filter()
print("\n .filter() \n")

df3 = df.groupby("Team").filter(lambda x : x ["Salary"].mean()>85)
print(df3)