import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#pip install Flask
"""from flask import Flask, request, jsonify
app = Flask(__name__)"""

pulgadas = np.array([ 1, 3, 7, 10, 15, 22, 26, 29, 32, 40], dtype=float)
centimetros = np.array([ 2.54, 7.62, 17.78, 25.4, 38.1, 55.88,
                         66.04, 73.66, 81.28, 101.6], dtype=float)

############ Sin capas ocultas ####################
#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo = tf.keras.Sequential([capa])

########### Con capas ocultas #####################
Entrada = tf.keras.layers.Dense(units=3, input_shape=[1])
Oculta1 = tf.keras.layers.Dense(units=3)
Salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([Entrada, Oculta1, Salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
    )

print("Comenzando entrenamiento...")

historial = modelo.fit(pulgadas, centimetros, epochs=1000, verbose=False)
print("Modelo entrenado")

plt.xlabel("No. Epoca")
plt.ylabel("MSE")
plt.plot(historial.history["loss"])

while True:
    print("Comencemos con las predicciones")
    dato = input("Qué dato quieres convertir?")
    if dato == "salir":
        break
    resultado = modelo.predict([float(dato)])
    print("La red predice: " + str(resultado) + "cm")

print("Cerrando Red")

""" creacion de la api http://localhost:5000/convertir
@app.route('/convertir', methods=['GET'])
def convertir_get():
    pulgada = request.args.get('pulgada')
    resultado = modelo.predict([float(pulgada)])
    return jsonify({'centimetros': resultado.tolist()})

@app.route('/convertir', methods=['POST'])
def convertir_post():
    data = request.get_json()
    pulgada = data['pulgada']
    resultado = modelo.predict([float(pulgada)])
    return jsonify({'centimetros': resultado.tolist()})

if __name__ == '__main__':
    app.run(debug=True)"""