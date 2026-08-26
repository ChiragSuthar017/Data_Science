import tensorflow as tf 
import matplotlib.pyplot as plt

# load data 
(x_train, y_train) , (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# check the shape
print("\ntraining data shape : ", x_train.shape)
print("\ntraining data shape : ", y_train.shape)

# plot first 10 images with labels 
plt.figure(figsize=(10, 2))
for i in range(10) :
    plt.subplot(1, 10, i+1)
    plt.imshow(x_train[i], cmap="gray")
    plt.axis("off")
    plt.title(str(y_train[i]))
plt.tight_layout()
plt.show()