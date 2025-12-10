import pandas as pd 

# insert a sample dataframe 
data = {
    'Name'      : ['Alice', 'bob', 'charlie'],
    'Math'      : [85,78,92],
    'Science'   : [92,82,89],
    'English'   : [88,85,94]
}
df  = pd.DataFrame(data)
print(df)

# melt()
print("\n melt() \n")

df2 = df.melt(id_vars=["Name"],value_vars=["Math","Science","English"],var_name="Subject",value_name="Score")
print(df2,"\n")
df2=df2.sort_values("Name")
print(df2)

# pivot()
print("\n pivot() \n")

df3 = df2.pivot(index="Name",columns="Subject",values="Score")
print(df3)