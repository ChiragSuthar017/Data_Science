import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_columns', None)
df = pd.read_csv("housing.csv")
# print(df.head(),"\n")
# print(df.tail())

# print(df.info())
# print(df['ocean_proximity'].value_counts())
# print(df.describe())

# create histograms graphs 
df.hist(bins = 50, figsize=(12,8))
plt.suptitle("California Housing Dataset - Feature Distributions", fontsize = 18)
plt.tight_layout(rect=[0, 0, 1, 0.96])
# plt.show() 

# create test set and train set 
def shuffle_and_split(data, test_ratio):
    np.random.seed(42) # set the seed for reproducibility
    shuffeld_indices = np.random.permutation(len(data)) # this return shuffle indices
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffeld_indices[:test_set_size]
    train_indices = shuffeld_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
train, test = shuffle_and_split(df, 0.2)

# create income categories for accurate shuffle  
df['income_cat'] = pd.cut(df["median_income"], bins = [0, 1.5, 3.0, 4.5, 6.0, np.inf], labels = [1, 2, 3, 4, 5])
# print(df.head())

df["income_cat"].value_counts().sort_index().plot.bar(rot = 0, grid = True)
plt.title("Income Category Distribution")
plt.xlabel("Income Category")
plt.ylabel("Number of Instances")
# plt.show()

# Assume income_cat is a colums in the dataset created from median_income
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(df, df['income_cat']):
    strat_train_set = df.loc[train_index]
    strat_test_set = df.loc[test_index]

# print(test)
# print(train)
df = df.drop("income_cat", axis=1)
strat_train_set["income_cat"].value_counts().sort_index().plot.bar(rot = 0, grid = True)
plt.title("Income Categories Distributions For Train DataSet")
plt.xlabel("Income Category")
plt.ylabel("Number of Instances")
# plt.show()

strat_test_set["income_cat"].value_counts().sort_index().plot.bar(rot = 0, grid = True)
plt.title("Income Categories Distributions For Test DataSet")
plt.xlabel("Income Category")
plt.ylabel("Number of Instances")
# plt.show()

# Remove the income_cat column
for sett in (strat_train_set, strat_test_set):
    sett.drop("income_cat", axis = 1, inplace = True)
# print(strat_train_set)

# create a copy of train data set 
data = strat_train_set.copy()
# print(data)

# create scatter plot 
data.plot(kind = "scatter", x = "latitude", y = "longitude", grid = True, cmap = "jet", c="median_house_value")
# plt.show()

# get correlation 
data.drop(labels="ocean_proximity", inplace=True, axis=1)
# print(data.corr())

attributes = ["housing_median_age", "median_income", "median_house_value"]
scatter_matrix(data[attributes], figsize=(12, 8))
# plt.show()

# separate labels 
housing = data.drop("median_house_value", axis = 1)
housing_labels = data["median_house_value"]
# print(housing)
# print(housing_labels)

# replace a NaN values into predict values
imputer = SimpleImputer(strategy="median")
housing_num = housing.select_dtypes(include=[np.number])
imputer.fit(housing_num)
# print(imputer.statistics_)
X = imputer.transform(housing_num)

# recreate data frame of housing_num
housing = pd.DataFrame(X, columns=housing_num.columns, index=housing_num.index)
# print(housing)

# add ocean_proximity column in housing data frame
housing['ocean_proximity'] = df['ocean_proximity']
# print(housing)

# change ocean_proximity datatype into numeric using ordinal encoder
print(set(housing['ocean_proximity'])) 
ordinal_encoder = OrdinalEncoder()
housing_cat = ordinal_encoder.fit_transform(housing)
housing_cat_ordinal = pd.DataFrame(housing_cat, columns=housing.columns, index=housing.index)
# print(housing_cat_ordinal)

# change ocean_proximity datatype into numeric using one-hot encoder
housing_ocean = housing[['ocean_proximity']]
one_hot = OneHotEncoder()
housing_cat = one_hot.fit_transform(housing_ocean)
# print(one_hot.categories_)
housing_cat_one_hot = pd.DataFrame(housing_cat.toarray(), columns=['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'], index=housing.index)
# print(housing_cat_one_hot)

data1 = df.copy()
# print(data1)
data1 = pd.concat([data1, housing_cat_one_hot], axis=1)
# print(data1)

# convert whole data into -1 to 1 
data1 = data1.drop("ocean_proximity", axis=1)
scaler = MinMaxScaler(feature_range=(-1,1))
data1_scaled = scaler.fit_transform(data1)
data1_scaled = pd.DataFrame(data1_scaled, columns= data1.columns, index=data1.index)
print(data1_scaled)

#standard scale
data2 = df.copy()
data2 = data2.drop("ocean_proximity", axis=1)
scaler = StandardScaler()
data2_scaled = scaler.fit_transform(data2)
data2_scaled = pd.DataFrame(data1_scaled, columns= data2.columns, index=data2.index)
print(data2_scaled)
