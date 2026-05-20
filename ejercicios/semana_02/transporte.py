class Transporte:
    def __init__(self, tipo, capacidad, velocidad_max, combustible, peso, color, longitud, fabricante, anio, precio):
        self.tipo = tipo
        self.capacidad = capacidad
        self.velocidad_max = velocidad_max
        self.combustible = combustible
        self.peso = peso
        self.color = color
        self.longitud = longitud
        self.fabricante = fabricante
        self.anio = anio
        self.precio = precio

        print(f"Tipo:{self.tipo}")
        print(f"Capacidad:{self.capacidad}")
        print(f"Velocidad Máxima:{self.velocidad_max}")
        print(f"Combustible:{self.combustible}")
        print(f"Peso:{self.peso}")
        print(f"Color:{self.color}")
        print(f"Longitud:{self.longitud}")
        print(f"Fabricante:{self.fabricante}")
        print(f"Año:{self.anio}")
        print(f"Precio:{self.precio}")

    def moverse(self): print(f"El {self.tipo} se está moviendo.")
    def detenerse(self): print(f"El {self.tipo} se detuvo.")
    def mostrar_informacion(self):
        print("Detalles de transporte")
        print(f"{self.tipo} - {self.fabricante} {self.anio}")
