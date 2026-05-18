clas Silla:
   def __init__(self, material, color, altura, peso, tipo, respaldo, ruedas,
               capacidad_carga, precio, fabricante):
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
