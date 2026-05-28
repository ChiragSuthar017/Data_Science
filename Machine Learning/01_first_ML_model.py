from  sklearn.tree import DecisionTreeClassifier

features = [[150, 0], [170 , 0],
            [130, 1], [120, 1]]

labels = ["apple", "apple", "orange", "orange"]

clf = DecisionTreeClassifier()
clf = clf.fit(features, labels)

prediction = clf.predict([[170, 0]])
print(f"The fruit is {prediction[0]}")

# VISULIZE IT 

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plot_tree(clf, feature_names=["weight", "color"], class_names=["apple", "orange"], filled=True)
plt.show()