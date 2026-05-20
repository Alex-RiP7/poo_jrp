class Coche:
    def __init__(self, marca, modelo, color, anio, placas, numero_puertas, velocidad_max, combustible, kilometraje, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.placas = placas
        self.numero_puertas = numero_puertas
        self.velocidad_max = velocidad_max
        self.combustible = combustible
        self.kilometraje = kilometraje
        self.precio = precio

        print(f"Marca:{self.marca}")
        print(f"Modelomodelo:{self.modelo}")
        print(f"Color:{self.color}")
        print(f"Año:{self.anio}")
        print(f"Placas:{self.placas}")
        print(f"Puertas:{self.puertas}")
        print(f"Velocidad Máxima:{self.velocidad_max}")
        print(f"Combustible:{self.combustible}")
        print(f"Kilometraje:{self.kilometraje}")
        print(f"Precio:{self.precio}")

    def enceder(self): print(f"El coche {self.marca} {self.modelo} se ha encendido.")
    def mover(self): print(f"{self.marca} {self.modelo} esta en movimiento.")
    def tocar_bocina(self):
        print("Pii piiip")
    def mostrar_informacion(self):
        print("Detalles de coche")
        print(f"{self.marca} {self.modelo} ({self.anio}) - {self.color}")
        print(f"Placas: {self.placas} | {self.kilometraje} km")
        
