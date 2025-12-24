import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# check data set in seaborn
print(sns.get_dataset_names()) 
# get data set from seaborn 
tips = sns.load_dataset('tips')
print(tips.head())

# Line plot
sns.lineplot(x = 'total_bill', y = 'tip', data=tips)
plt.title('Line plot example')
plt.show()

# Scatter plot
sns.scatterplot(x = 'total_bill', y = 'tip', data=tips)
plt.title('Scatter plot example')
plt.show()

# Bar plot
sns.barplot(x = 'total_bill', y = 'tip', data=tips)
plt.title('Bar plot example')
plt.show()

# Box plot
sns.boxplot(x = 'total_bill', y = 'tip', data=tips)
plt.title('Box plot example')
plt.show()

# Heatmap (Correlation Matrix)

flights = sns.load_dataset('flights') # get another data from seaborn
pivot_table = flights.pivot(index='month', columns='year', values='passengers')
print(pivot_table)

sns.heatmap(pivot_table, annot=True, fmt='d', cmap='viridis')
plt.title('Heatmap of passengers')
plt.show()

# Working with pandas dataframes

df = pd.DataFrame({
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 34, 43],
    "salary": [25000, 27000, 52000, 60000, 58000, 62000, 61000, 65000, 38000, 45000],
    "gender": ["M", "F", "M", "F", "F", "M", "M", "F", "F", "M"]
})
 
sns.scatterplot(x="age", y="salary", hue="gender", data=df)
plt.title('Salary vs Age Scatter Plot')
for i in range(len(df)):
    plt.annotate(f'e{i+1}',(df['age'][i],df['salary'][i]))
plt.show()