import matplotlib.pyplot as plt
import numpy as np

# Arreglos con las coordenadas para cada letra (diccionario)
dictionary = {
    "c": np.array([[10, 0 ], [0, 0 ], [ 0, 10], [10, 10]]),
    "r": np.array([[ 5, 0 ], [5, 10], [ 5, 8 ], [ 8,  9], [ 9,  8]]),
    "i": np.array([[ 5, 0 ], [5, 10]]),
    "s": np.array([[ 0, 0 ], [5, 0 ], [ 5, 5], [ 0, 5], [ 0, 10], [ 5, 10]]),
    "t": np.array([[ 5, 0 ], [5, 10], [ 0, 10],[10, 10]]),
    "h": np.array([[ 5, 0 ], [5, 10], [ 5, 5], [10, 5], [10, 0], [10, 10], [10, 5]]),
    "I": np.array([[ 5, 0 ], [5, 10]]),
    "a": np.array([[ 0, 0 ], [5, 10], [10, 0], [7.5, 5], [2.5, 5]]),
    "n": np.array([[ 0, 0 ], [0, 10], [10, 0], [10, 10]]),
    "e": np.array([[10, 0 ], [0, 0 ], [ 0, 10], [10, 10],[0, 10],[0, 5],[10, 5]]),
    "l": np.array([[10, 0 ], [0, 0 ], [ 0, 10]]),
    "u": np.array([[ 0, 10], [0, 0 ], [10,  0], [10,  10]]),
    "d": np.array([[ 0, 0 ], [0, 10], [10,  5], [ 0,   0]]),
    "g": np.array([[10, 10], [0, 10], [ 0,  0], [10,   0], [10, 5], [0, 5]]),
    "o": np.array([[ 0,  0], [0, 10], [10, 10], [10,   0], [ 0, 0 ]]),
}

# Lista de nombres con sus posiciones iniciales (tupla)
nombres = [
    ("cristian", 0, 0),
    ("daniel", 0, -15),
    ("diego", 0, -30),
    ("nicolas", 0, -45)
]
#(Creo figura "fig" y conjunto de ejes "ax")
fig, ax = plt.subplots() 

# Función para dibujar una letra en una posición específica
def dibujar_letra(ax, letra, x, y):
    coords = dictionary[letra]
    ax.plot(coords[:, 0] + x, coords[:, 1] + y)

# Espaciado entre letras 
espaciado_letras = 12  

# Iterar sobre los nombres y dibujarlos
for nombre, x_offset, y_offset in nombres:
    x_pos = x_offset
    for letra in nombre:
        dibujar_letra(ax, letra, x_pos, y_offset)
        x_pos += espaciado_letras  # Espaciado entre letras

ax.set_xlim([-5, 120])
ax.set_ylim([-55, 20])
ax.set_aspect("equal")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Nombres en 2D")
plt.show()
