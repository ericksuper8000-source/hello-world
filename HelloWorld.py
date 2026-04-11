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

Set_Conjunto1 = {1, 2, 3}
Set_Conjunto2 = set({'Pera', 'Manzana'})
Set_Conjunto2.add('Banana')

print (f'Naranja' in Set_Conjunto2)

print (f'{Set_Conjunto2}')

print (f'-' * 20)

# operaciones de conjuntos, encontrar la intercepcion de dos conjuntos ------------

amigos_jose = {'jose', 'maria', 'roberto'}
amigos_pedro = {'carlos', 'roberto', 'jose'}

print (f'{amigos_jose.intersection(amigos_pedro)}')

# Ejercicio_pertenece_obtener ------------

elemento = 'Carlos'

coleccion = {'Maria', 'Roberto', 'Juan', 'Liliana', 'Carlos'}

pertenece = False

buscar = 'Carlos' in coleccion

if (buscar == True):
    print (f'Encontrado')
else:
    print (f'No encontrado')

for indice, elemento in enumerate(coleccion, start=1):
    if (elemento == 'Carlos'):
        pertenece = True
        if (pertenece == True):
            print(f'{elemento} fue encontrado')
            break
        else:
            print (f'No pertenece')
    else:
        pertenece = False
        continue


