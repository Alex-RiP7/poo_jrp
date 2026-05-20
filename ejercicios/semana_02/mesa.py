class Mesa:
    def __init__(self, material, forma, longitud, ancho, altura, color,capacidad_personas, peso, precio, ubicacion):
        self.material = material
        self.forma = forma
        self.longitud = longitud
        self.ancho = ancho
        self.altura = altura
        self.color = color
        self.capacidad_personas = capacidad_personas
        self.peso = peso
        self.precio = precio
        self.ubicacion = ubicacion

        print("=== INFORMACIÓN DE LA MESA ===")
        print(f"Material: {self.material}")
        print(f"Forma: {self.forma}")
        print(f"Dimensiones: {self.longitud} x {self.ancho} x {self.altura} cm")
        print(f"Color: {self.color}")
        print(f"Capacidad: {self.capacidad_personas} personas")
        print(f"Peso: {self.peso} kg")
        print(f"Precio: {self.precio}")
        print(f"Ubicación: {self.ubicacion}")

    def colocar_objetos(self): print("Objetos colocados sobre la mesa.")
    def limpiar(self): print("Mesa limpiada.")
    def mostrar_informacion(self):
        print("DETALLES DE LA MESA")
        print(f"{self.forma} de {self.material} - {self.capacidad_personas} personas")
        