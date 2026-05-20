class PersonajeVideojuego:
    def __init__(self, nombre, juego, raza, arma_principal, poder_especial, color_cabello, color_ojos, altura, fuerza, afinidad):
        self.nombre = nombre
        self.juego = juego
        self.raza = raza
        self.arma_principal = arma_principal
        self.poder_especial = poder_especial
        self.color_cabello = color_cabello
        self.color_ojos = color_ojos
        self.altura = altura
        self.fuerza = fuerza
        self.afinidad = afinidad

        print(f"Nombre:{self.nombre}")
        print(f"Juego:{self.juego}")
        print(f"Raza:{self.raza}")
        print(f"Arma Principal:{self.arma_principal}")
        print(f"Poder Especial:{self.poder_especial}")
        print(f"Cabello:{self.color_cabello}")
        print(f"Ojos:{self.color_ojos}")
        print(f"Altura:{self.altura}")
        print(f"Fuerza:{self.fuerza}")
        print(f"Afinidad:{self.afinidad}")

    def atacar(self):
        print(f" {self.nombre} realiza un poderoso ataque con {self.arma_principal}")
    def usar_poder_especial(self):
        print(f" {self.nombre} activa su poder especial: {self.poder_especial}")
    def mostrar_informacion(self):
        print("Detalles del personaje")
        print(f"{self.nombre} de {self.juego} | {self.raza}")
        print(f"Fuerza: {self.fuerza} | Arma: {self.arma_principal}")
