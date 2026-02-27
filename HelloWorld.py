class Pokemon:
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = not True

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

class Poke2(Pokemon):
    def __init__(self, Nombre, Tipo, Ataque, City, SubTipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.City = City
        self.SubTipo = SubTipo

    def Desplegar(self):
        print (f'{self.Nombre} habita {self.City} y es de tipo {self.Tipo} / {self.SubTipo}')

Objeto1 = Poke2('Pikachu', 'Electrico', 'Impact Trueno', 'Paldea', 'Acero')

Objeto1.Mostrar()

Objeto1.Desplegar()

Lista = list(['Erick', 'Josue', 'Karlita'])

i = 0

Diccionario1 = dict.fromkeys(['Uno', 'Dos', 'Tres'])

for elemento in Diccionario1.items():
    Diccionario1[elemento[0]] = Lista[i]
    i+= 1

print (f'{Diccionario1}')

import pandas as pd

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv.head()}')

Llaves = [f'Llave{i}' for i in range(len(Cargar_Csv))]

print (f'{Llaves}')

Nombres = list(Cargar_Csv["Nombre"])

print (f'{Nombres}')

Diccionario2 = dict(zip(Llaves, Nombres))

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2["Llave0"]}')
print (f'{Diccionario2.get("Llave1")}')