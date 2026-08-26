import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("housing.csv")
# print(df)
# print(df['ocean_proximity'].value_counts())

# create test set and train set 

df['income_cat'] = pd.cut(df['median_income'], bins=[0,1.5,3.0,4.5,6.0,np.inf], labels=[1,2,3,4,5])
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2,random_state=42)
for train_index, test_index in split.split(df,df['income_cat']):
    strat_train_set = df.loc[train_index]
    strat_test_set = df.loc[test_index]
# print(strat_train_set)
# print(strat_test_set)

# remove income_cat column
for sett in (strat_train_set, strat_test_set):
    sett.drop("income_cat", axis=1, inplace=True)
train_data = strat_train_set.copy()
# print(train_data)

# separate labels 
housing = train_data.drop('median_house_value', axis=1)
housing_labels = train_data['median_house_value']
# print(housing)
# print(housing_labels)

# create pipeline
housing = housing.drop('ocean_proximity', axis=1)
# print(housing)
mypipeline = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("standardize", StandardScaler()),
])
mypipeline.fit_transform(housing)
print(housing)