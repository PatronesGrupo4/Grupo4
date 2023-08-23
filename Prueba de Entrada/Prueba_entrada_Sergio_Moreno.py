import numpy as np

# Pregunta 1

numeros = [5, -2, 10, -8, 3, -6, 0, 7, -4, 1]

numeros_negativos = []

for numero in numeros:
    if numero < 0:
        numeros_negativos.append(numero)

print("Valores negativos:", numeros_negativos)

# Pregunta 2

numeros_float = np.random.rand(3, 3)

matriz_3x3 = numeros_float.reshape(3, 3)

print("Matriz 3x3:")
print(matriz_3x3)

# Pregunta 3

matriz_A = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matriz_B = np.array([[2],
                     [3],
                     [1]])

matriz_C = np.array([[5],
                     [6],
                     [7]])

resultado = np.dot(matriz_A, matriz_B) + matriz_C

print("Resultado de AxB + C:")
print(resultado)

# Pregunta 4

numeros = list(range(1, 101))

for i in range(len(numeros)):
    if numeros[i] % 3 == 0:
        numeros[i] = "m3"

print(numeros)
