try:
    import Module_Own as PEPE
except ImportError:
    print (f'El paquete es incorrecto')

from Module_Own import Pokemon as Poke

class Poke_Hija(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

    def Desplegar(self):
        print (f'{self.Nombre} es de tipos {self.Tipo}/{self.Sub_Tipo}')

Objeto1 = Poke_Hija(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno', 'Acero')
Objeto2 = Poke_Hija(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Hada')
Objeto3 = Poke_Hija(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Psiquico')

Poke.Mostrar(Objeto3)
Objeto3.Mostrar()
Objeto3.Desplegar()

print (f'----------------')

Poke.Mostrar(Objeto1)
Objeto1.Mostrar()
Objeto1.Desplegar()

print (f'----------------')

Poke.Mostrar(Objeto2)
Objeto2.Mostrar()
Objeto2.Desplegar()

print (f'----------------')

class Camara():
    def Tomar_Fotografia(self):
        print (f'FOTOGRAFIA TOMADA')

class Reproductor_Musica:
    def Reproducir_Musica(self):
        print (f'MUSICA REPRODUCIDA')

class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'SMARTPHONE ENCENDIDO')

Objeto4 = Smartphone()

Objeto4.Encender_Smartphone()
Objeto4.Reproducir_Musica()
Objeto4.Tomar_Fotografia()

print (f'----------------')

class Mascota():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')

class Perro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento, Visitas):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        self.Visitas = Visitas

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        print (f'Visitas: {self.Visitas} visitas en el mes')

Objeto5 = Perro('Chester', 3, 1.8, 'Poodle', 'Hipertension', 3)

Mascota.Mostrar(Objeto5)
Objeto5.Mostrar()

print (f'----------------')

class Gato(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo} esta activo')

Objeto6 = Gato('Messi', 2, 1.2, 'Angora', 'Gris', 'Si')

Mascota.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'----------------')

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla} habla')

Objeto7 = Pajaro('Polly', 31, 0.4, 'Lora Verde', 'Si')

Mascota.Mostrar(Objeto7)
Objeto7.Mostrar()

print (f'----------------')

class Atacante():
    def __init__(self, Damage, Weapon, Attack_Energy):
        self.Damage = Damage
        self.Weapon = Weapon
        self.Attack_Energy = Attack_Energy

    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        print (f'Attack_Energy: {self.Attack_Energy}')

class Curador:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}')

class Paladin(Atacante, Curador):
    def __init__(self, Damage, Weapon, Attack_Energy, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon, Attack_Energy)
        Curador.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto8 = Paladin(125, 'Espada Diamante', 30, 25, 'Pocion de esmeralda', 500, 'Ghost Knight')

Objeto8.Mostrar()
Atacante.Mostrar(Objeto8)
Curador.Mostrar(Objeto8)

print (f'----------------')

Clase_Hija = issubclass(Poke_Hija, Poke)

print (f'{Clase_Hija}')

Objeto_Clase = isinstance(Objeto8, Atacante)

print (f'{Objeto_Clase}')

print (f'----------------')

