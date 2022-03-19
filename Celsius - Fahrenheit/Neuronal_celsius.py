import tensorflow as tf
import numpy as np
from os import system as sys

sys("cls")

"""import matplotlib.pyplot as plt"""

# Variables de entrenamiento
# Training variables
celsius = np.array(
    [
        -200,
        -175,
        -150,
        -125,
        -100,
        -75,
        -50,
        -25,
        0,
        25,
        50,
        75,
        100,
        125,
        150,
        175,
        200,
    ],
    dtype=float,
)
fahrenheit = np.array(
    [
        -328,
        -283,
        -238,
        -193,
        -148,
        -103,
        -58,
        -13,
        32,
        77,
        122,
        167,
        212,
        257,
        302,
        347,
        392,
    ],
    dtype=float,
)

# Aquí se crean las capas de las redes neuronales
# Create the neural networks
ocular1 = tf.keras.layers.Dense(units=3, input_shape=[1])
ocular2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([ocular1, ocular2, salida])

# Aquí se compila el modelo de entrenamiento
# Compile the training model
modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss="mean_squared_error")

# **¡¡¡EMPEZAR EL ENTRENAMIENTO!!!**
#     **¡¡¡START TRAINING!!!**
print("Comenzando entrenamiento...\n")  # starting training
historial = modelo.fit(celsius, fahrenheit, epochs=300, verbose=False)
print("Modelo entrenado!")  # the model has been trained


"""# Muestra un gráfico indicando la cantidad de errores que hubieron
plt.xlabel('# Epoca')
plt.ylabel('Magnitud de perdida')
plt.plot(historial.history['loss'])"""


# **Pon a prueba la prediccion**
#    **Test the prediction**
print("\n\nHagamos una prediccion!\n")  # let's make a prediction
print("Escribe los grados Celsius:")  # write the celsius degrees

inPut = float(input())
result = modelo.predict([inPut])
print("\nEl resultado de " + str(inPut) + "°C es " + str(result) + "°F\n")
