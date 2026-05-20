# Casa.py

class Casa:
    def __init__(self, direccion, color, numero_pisos, habitaciones, banos,
                 area_construida, garage, jardin, anio_construccion, precio):
                   
        self.direccion = direccion
        self.color = color
        self.numero_pisos = numero_pisos
        self.habitaciones = habitaciones
        self.banos = banos
        self.area_construida = area_construida
        self.garage = garage
        self.jardin = jardin
        self.anio_construccion = anio_construccion
        self.precio = precio

        print(f"Direccion: {self.direccion}")
        print(f"Color: {self.color}")
        print(f"Pisios: {self.numero_pisos}")
        print(f"Habitaciones: {self.habitaciones}")
        print(f"Baños: {self.banos}")
        print(f"Área construida: {self.area_construida}")
        print(f"Garage: {self.garage}")
        print(f"Jardín: {self.jardin}")
        print(f"Año de construcción: {self.anio_construccion}")
        print(f"Precio: {self.precio}")

    def abrir_puerta(self):
        print("Puerta principal abierta.")

    def encender_luces(self):
        print("Luces encendidas.")

    def mostrar_informacion(self):
        print("Detalles de la casa")
        print(f"{self.direccion} | {self.habitaciones} habitaciones")
              