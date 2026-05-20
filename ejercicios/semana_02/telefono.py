class Telefono:
    def __init__(self, marca, modelo, color, ram, almacenamiento, camara, bateria, sistema, pantalla, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.camara = camara
        self.bateria = bateria
        self.sistema = sistema
        self.pantalla = pantalla
        self.precio = precio

        print(f"Marca:{self.marca}")
        print(f"Modelo:{self.modelo}")
        print(f"Color:{self.color}")
        print(f"Ram:{self.ram}")
        print(f"Almacenamiento:{self.almacenamiento}")
        print(f"Cámara:{self.camara}")
        print(f"Batería:{self.bateria}")
        print(f"Sistema:{self.sistema}")
        print(f"Pantalla:{self.pantalla}")
        print(f"Precio:{self.precio}")

    def llamar(self): print("Realizando llamada")
    def tomar_foto(self): print("Foto tomada.")
    def mostrar_informacion(self):
        print("Detalles del teléfono")
        print(f"{self.marca} {self.modelo} - {self.precio}")
