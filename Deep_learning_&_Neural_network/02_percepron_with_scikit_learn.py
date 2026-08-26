from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

x,y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
x_train , x_test, y_train, y_teat = train_test_split(x,y, random_state=42)

clf = Perceptron(
    max_iter=1000,      # maximum number of epochs
    eta0=0.1,           # learning rate
    random_state=42,    # for reproducibility 
    tol=1e-3,           # stop early is improvement is smaller then this 
    shuffle=True        # shuffer data each epochs
)

clf.fit(x_train, y_train)

accuracy = clf.score(x_train, y_train)
print(f"Accuracy {accuracy:.2f}")