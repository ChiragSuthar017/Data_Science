import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

data = pd.read_excel("iris_train.xlsx")
# print(data)
x = data.iloc[:, :-1]  # All columns except the last as features
y = data.iloc[:, -1] # Last column as label

model = RandomForestClassifier()
model.fit(x.values , y.values)

predictions = model.predict(x.values) # predict all rows in x 
# print(predictions)
prediction = model.predict([[0.4, 0.7, 20, 0.43]]) # predict  only who i write 
# print(prediction)


# Measuring Accurasy of our prediction 

dataset = pd.read_excel("iris_test.xlsx")
x_test = dataset.iloc[:, : -1]
pre = model.predict(x_test.values)
y_test = dataset.iloc[:, -1]
actual = y_test.values

count = 0

for i in range(0, len(actual)):
    if actual [i] == pre[i] :
        count += 1 
print((count * 100)/ len(actual))