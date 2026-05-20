class Silla:
        def __init__(self, material, color, altura, peso, tipo, respaldo, ruedas,capacidad_carga, precio, fabricante):
                self.material = material
                self.color = color
                self.altura = altura
                self.peso = peso
                self.tipo = tipo
                self.respaldo = respaldo
                self.ruedas = ruedas
                self.capacidad_carga = capacidad_carga
                self.precio = precio
                self.fabricante = fabricante

                print(f"Material: {self.material}")
                print(f"Color: {self.color}")
                print(f"Altura: {self.altura} cm")
                print(f"Peso: {self.peso} kg")
                print(f"Tipo: {self.tipo}")
                print(f"Respaldo: {self.respaldo}")
                print(f"Ruedas: {self.ruedas}")
                print(f"Capacidad de carga: {self.capacidad_carga} kg")
                print(f"Precio: {self.precio}")
                print(f"Fabricante: {self.fabricante}")
                
        def sentarse(self): print(" Alguien se sentó en la silla.")
        def ajustar_altura(self): print(" Altura de la silla ajustada.")
        def mostrar_informacion(self):
            print("DETALLES DE LA SILLA")
            print(f"{self.tipo} de {self.material} - {self.color}")
