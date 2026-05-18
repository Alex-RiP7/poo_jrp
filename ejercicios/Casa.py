# Casa.py

class Casa:
    def __init__(self, direccion, color, numero_pisos, habitaciones, banos,
                 area_construida, garage, jardin, anio_construccion, precio):
                   
        self.direccion = direccion
        self.color = color
        self.numero_pisos = numero_pisos
        self.habitaciones = habitaciones
        self.banos = banos
        self.area_construida = area_contruida
        self.garage = garaje
        self.jardin = jardin
        self.anio_construccion = anio_construccion
        self.precio = precio

    def abrir_puerta(self):
        print("Puerta principal abierta.")

    def encender_luces(self):
        print("Luces encendidas.")

    def mostrar_informacion(self):
        print("Detalles de la casa)
        print(f"{self.direccion} | {self.habitaciones} habitaciones")
              
