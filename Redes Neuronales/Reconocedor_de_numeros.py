from __future__ import absolute_import, division, print_function, unicode_literals
from os import system
import tensorflow as tf, tensorflow_datasets as tfds, math, numpy as np, matplotlib.pyplot as plt, logging

logger = tf.get_logger()
logger.setLevel(logging.ERROR)


dataset, metadata = tfds.load("mnist", as_supervised=True, with_info=True)
train_dataset, test_dataset = dataset["train"], dataset["test"]

class_names = [
    "Cero",
    "Uno",
    "Dos",
    "Tres",
    "Cuatro",
    "Cinco",
    "Seis",
    "Siete",
    "Ocho",
    "Nueve",
]

num_train_examples = metadata.splits["train"].num_examples
num_test_examples = metadata.splits["test"].num_examples

system("cls")
print("\nStarting...\n\n")

# Normalizar: Numeros de 0 a 255, que sean de 0 a 1
def normalize(images, labels):
    images = tf.cast(images, tf.float32)
    images /= 255
    return images, labels


train_dataset = train_dataset.map(normalize)
test_dataset = test_dataset.map(normalize)

# Estructura de la red
model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
        tf.keras.layers.Dense(50, activation=tf.nn.relu),  # 1
        tf.keras.layers.Dense(50, activation=tf.nn.relu),  # 2
        tf.keras.layers.Dense(50, activation=tf.nn.relu),  # 3
        tf.keras.layers.Dense(10, activation=tf.nn.softmax),
    ]
)

# Indicar las funciones a utilizar
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# Aprendizaje por lotes de 32 cada lote
BATCHSIZE = 32
train_dataset = train_dataset.repeat().shuffle(num_train_examples).batch(BATCHSIZE)
test_dataset = test_dataset.batch(BATCHSIZE)

# Realizar el aprendizaje
model.fit(
    train_dataset, epochs=5, steps_per_epoch=math.ceil(num_train_examples / BATCHSIZE)
)

# Evaluar nuestro modelo ya entrenado, contra el dataset de pruebas
test_loss, test_accuracy = model.evaluate(
    test_dataset, steps=math.ceil(num_test_examples / 32)
)

print("\n\nResultado de las pruebas: ", test_accuracy, "\n")

for test_images, test_labels in test_dataset.take(1):
    test_images = test_images.numpy()
    test_labels = test_labels.numpy()
    predictions = model.predict(test_images)


def plot_image(i, predictions_array, true_labels, images):
    predictions_array, true_label, img = predictions_array[i], true_labels[i], images[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img[..., 0], cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = "green"
    else:
        color = "red"

    plt.xlabel("Prediction: {}".format(class_names[predicted_label]), color=color)


def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#888888")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color("red")
    thisplot[true_label].set_color("green")


numrows = 5
numcols = 4
numimages = numrows * numcols

plt.figure(figsize=(2 * 2 * numcols, 2 * numrows))
for i in range(numimages):
    plt.subplot(numrows, 2 * numcols, 2 * i + 1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(numrows, 2 * numcols, 2 * i + 2)
    plot_value_array(i, predictions, test_labels)

plt.show()
