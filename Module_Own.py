Diccionario_Pokemon = dict.fromkeys(['Poke1', 'Poke2', 'Poke3'])

Set_Conjunto_Poke1 = set({'Pikachu'})
Set_Conjunto_Poke1.add('Graveler')
Set_Conjunto_Poke2 = {'Vaporeon'}

Set_Conjunto_Poke1.update(Set_Conjunto_Poke2)

for elemento in Set_Conjunto_Poke1:
    if (elemento == 'Pikachu'):
        Diccionario_Pokemon['Poke1'] = elemento
    elif (elemento == 'Graveler'):
        Diccionario_Pokemon['Poke2'] = elemento
    elif (elemento == 'Vaporeon'):
        Diccionario_Pokemon['Poke3'] = elemento
    else:
        continue

class Pokemon1():
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = not True

    def Mostrar1(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')
     
    @property   
    def Mostrar2(self):
        return self.Nombre
    
    def __str__(self):
        return self.Nombre