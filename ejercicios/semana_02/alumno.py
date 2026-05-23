class Alumno:
    def __init__(self, nombre, matricula, carrera, semestre, edad, 
                 genero, promedio, email_institucional, telefono, estatus):
        
        # 10 Atributos
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        self.edad = edad
        self.genero = genero
        self.promedio = promedio
        self.email_institucional = email_institucional
        self.telefono = telefono
        self.estatus = estatus  # Activo, Baja temporal, Graduado, etc.

        print("=== INFORMACIÓN DEL ALUMNO ===")
        print(f"Nombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        print(f"Edad: {self.edad} años")
        print(f"Género: {self.genero}")
        print(f"Promedio: {self.promedio}")
        print(f"Email Institucional: {self.email_institucional}")
        print(f"Teléfono: {self.telefono}")
        print(f"Estatus: {self.estatus}")
        print("================================\n")

    def estudiar(self):
        print(f"📚 {self.nombre} está estudiando para el próximo examen.")

    def inscribir_materia(self, materia):
        print(f"✅ {self.nombre} se ha inscrito a la materia: {materia}")

    def mostrar_informacion(self):
        print("=== DETALLES DEL ALUMNO ===")
        print(f"{self.nombre} | Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera} | Semestre: {self.semestre} | Promedio: {self.promedio}")
        print(f"Estatus: {self.estatus}")
        print("================================\n")

    def entregar_tarea(self, tarea):
        print(f"📝 {self.nombre} entregó la tarea: {tarea}")

    def ver_kardex(self):
        print(f"📋 Mostrando kardex del alumno {self.nombre} (Matrícula: {self.matricula})")