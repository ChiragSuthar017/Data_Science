import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the input data
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-Hot encode the labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Build a Simple Neural NEtwork
model = Sequential([
    Flatten(input_shape=(28, 28)), # 28x28 images to 784 input feature
    Dense(128, activation='relu'), # Hidden layer with 128 newrones
    Dense(10, activation='softmax') # Output layer for 10 classes
])

# Compiling the model 
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
) 

# Training the model
model.fit(x_train, y_train, epochs = 5, batch_size = 32)

# Evalute the model
test_loss , test_acc = model.evaluate(x_test, y_test)
print(f"\nTest accuracy: {test_acc:.4f}")