class Perro:
    def __init__(self, nombre, raza, edad, color, peso, altura, genero, temperamento, vacunado, dueno):
        self.nombre = nombre
        self.raza =raza
        self.edad = edad
        self.color = color
        self.peso =peso
        self.altura = altura
        self.genero = genero
        self.temperamento = temperamento
        self.vacunado = vacunado
        self.dueno = dueno

        print(f"Nombre:{self.nombre}")
        print(f"Raza:{self.raza}")
        print(f"Edad:{self.edad}")
        print(f"Color:{self.color}")
        print(f"Peso:{self.peso}")
        print(f"Altura:{self.altura}")
        print(f"Género:{self.genero}")
        print(f"Temperamento:{self.temperamento}")
        print(f"Vacunado:{self.vacunado}")
        print(f"Dueño:{self.dueno}")

    def ladrar(self):
        print(f"Guau Guau ({self.nombre} esta ladrando.)")
    def comer(self):
        print(f"{self.nombre} está comiendo.")
    def jugar(self):
        print(f"{self.nombre} está jugando felizmente.")
    def mostrar_informacion(self):
        print(f"{self.nombre} - {self.raza} ({self.edad} años) | {self.color}")
        