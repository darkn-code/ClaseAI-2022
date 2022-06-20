import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf

from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

def main():
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels)=fashion_mnist.load_data()

    print(train_images.shape)

    class_names = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]

    plt.figure()
    plt.imshow(train_images[100])
    plt.grid(True)
    plt.show()

    train_images = train_images /255.0
    test_images = test_images / 255.0

    plt.figure(figsize = (10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid("off")
        plt.imshow(train_images[i],cmap = plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

    model = keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),keras.layers.Dense(128,activation=tf.nn.relu),keras.layers.Dense(10,activation=tf.nn.softmax)])
    model.compile(optimizer=keras.optimizers.Adam(), loss="sparse_categorical_crossentropy",metrics=["accuracy"])
    model.fit(train_images,train_labels,epochs = 5)

    test_loss,test_acc = model.evaluate(test_images,test_labels)
    print("Accuracy",test_acc)

    predictions = model.predict(test_images)

    plt.figure(figsize = (10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid("off")
        plt.imshow(test_images[i],cmap = plt.cm.binary)
        predicted_label = np.argmax(predictions[i])
        true_label=test_labels[i]
        if predicted_label == true_label:
            color="blue"
        else:
            color="red"
        plt.xlabel("{} ({})".format(class_names[predicted_label],class_names[true_label]),color=color)
    plt.show()
if __name__ == "__main__":
    main()
