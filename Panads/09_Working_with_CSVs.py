import pandas as pd

# Read csv file
print("\n Read csv file \n")
df = pd.read_csv(r"D:\Data_Science\Panads\data1.csv")
print(df)

df = df[df['IMDb']>6.0]
print(df)

# Write csv file 
print("\n Write csv file \n")

df.to_csv("data_updates.csv")
df.to_csv("data_updates_noIndex.csv",index=False)

# Read Excel file 
print("\n Read Excel \n")

df1 = pd.read_excel(r"D:\Data_Science\Panads\data.xlsx")
print(df1)

# Write excel file 
# df1.to_excel("data1.xlsx")

# for multiple sheets

# with pd.ExcelWriter("report.xlsx") as writer:
#     df1.to_excel(writer, sheet_name="Summary", index=False)
#     df2.to_excel(writer, sheet_name="Details", index=False)

# read json file 
print("\n raed json file")

df2 = pd.read_json(r"D:\Data_Science\Panads\data.json")
print(df2,"\n")

data = [
{"name": "chirag" , "lan": {"basic" : "python" , "not basic" : "css"}},
{"name": "bhavy" , "lan": {"basic" : "c" , "not basic" : "c++"}}
]
df2 = pd.json_normalize(data)  
print(df2)