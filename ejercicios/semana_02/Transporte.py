class Univiersidad:
    def __init__(self, nombre, localidad, rector, carreras, alumnos, campus, fundacion, tipo, pagina_web, telefono):
        self.nombre = nombre
        self.localidad = localidad
        self.rector = rector
        self.carreras = carreras
        self.alumnos = alumnos
        self.campus = campus
        self.fundacion = fundacion
        self.tipo = tipo
        self.pagina_web = pagina_web
        self.telefono = telefono

        print(f"Nombre:{self.nombre}")
        print(f"Localidad:{self.localidad}")
        print(f"Rector:{self.rector}")
        print(f"Carreras:{self.carreras}")
        print(f"Alumnos:{self.alumnos}")
        print(f"Campus:{self.campus}")
        print(f"Año de fundación:{self.fundacion}")
        print(f"Tipo:{self.tipo}")
        print(f"Página web:{self.pagina_web}")
        print(f"Teléfono:{self.telefono}")

    def moverse(self): print(f"El {self.tipo} se está moviendo.")
    def detenerse(self): print(f"El {self.tipo} se detuvo.")
    def mostrar_informacion(self):
        print("Detalles de transporte")
        print(f"{self.tipo} - {self.fabricante} {self.anio}")
        