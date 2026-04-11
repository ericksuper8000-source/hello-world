import localstack_cli.utils.objects

Lista_Matriz = [[1, 2, 3], [4, 5, 6]]

print (f'{Lista_Matriz[0][1]}')

import numpy as np

Array1 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array1[0, 1]}')

Diccionario1 = {
    'Nombre' : "Erick",
    'Edad' : 37,
    'Votante' : not True
}

for elemento in Diccionario1.items():
    print (f'{elemento[0]} - {elemento[1]}')

print (f'-' * 20)

.keys()
.values()
.items()