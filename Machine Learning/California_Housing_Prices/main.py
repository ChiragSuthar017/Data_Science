import time
start = time.perf_counter()
import pandas as pd
import numpy as np
from sklearn.model_selection import  StratifiedShuffleSplit 
from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score

# 1. load the data 
data = pd.read_csv("housing.csv")

# 2. create a stratified test and train set based on income category 
data["income_cat"] = pd.cut(data["median_income"], bins=[0.0, 1.5, 3.0, 4.5, 6, np.inf], labels=[1,2,3,4,5])

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index , test_index in split.split(data ,data["income_cat"]):
    strat_train_set = data.loc[train_index].drop("income_cat", axis =1 ) # we work on this data 
    strat_test_set = data.loc[test_index].drop("income_cat", axis =1 )

# work on a copy of traning data
housing = strat_train_set.copy()

# 3. separate predictors and labels 
housing_labels = housing["median_house_value"].copy()
housing = housing.drop("median_house_value", axis = 1)

# 4. separate numerical and categorical columns 
num_attribs = housing.drop("ocean_proximity", axis = 1).columns.tolist()
cat_attribs = ["ocean_proximity"]

# 5. pipeline
# numerical pipeline
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

# categorical pipeline
cat_pipeline = Pipeline([
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# full pipeline
full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs),
])

# 6. tansform the data 
housing_prepared = full_pipeline.fit_transform(housing)
# hosing_ prepared is now numpy array ready for traning 
# print(housing_prepared) 

# 7. train the model
# linear regression 
lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)

# Decision tree
tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)

# Random Forest
forest_reg = RandomForestRegressor()
forest_reg.fit(housing_prepared, housing_labels)

# Predict using traning data
lin_preds = lin_reg.predict(housing_prepared)
tree_preds = tree_reg.predict(housing_prepared)
forest_preds = forest_reg.predict(housing_prepared)

# Calculate RMSE
lin_rmse = root_mean_squared_error(housing_labels, lin_preds)
tree_rmse = root_mean_squared_error(housing_labels, tree_preds)
forest_rmse = root_mean_squared_error(housing_labels, forest_preds)

print("Linear Regression RMSE : ", lin_rmse)
print("Decision Tree RMSE : ", tree_rmse)
print("Random Forest RMSE : ", forest_rmse)

# Cross-Validation
lin_rmses = -cross_val_score(lin_reg, housing_prepared, housing_labels, scoring="neg_root_mean_squared_error", cv=10)
tree_rmses = -cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_root_mean_squared_error", cv=10)
forest_rmses = -cross_val_score(forest_reg, housing_prepared, housing_labels, scoring="neg_root_mean_squared_error", cv=10)

# WARNING: Scikit-Linear's scoring uses utility functions (higher is better), so RMSE is returned as negative.
# We use minus (-) to convert it back to positive RMSE.

# print("Linear Regression cv RMSEs", lin_rmses)
print("\n Cross-Validation Performance ")
print("\n Cross-Validation for Linear Regression")
print(pd.Series(lin_rmses).describe())
print("\n Cross-Validation for Decision Tree")
print(pd.Series(tree_rmses).describe())
print("\n Cross-Validation for Random Forest")
print(pd.Series(forest_rmses).describe())

end = time.perf_counter()
print(f"Runtime: {end - start:.4f} seconds")