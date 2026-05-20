class Libro:
    def __init__(self,titulo, autor, isbn, editorial, anio, genero, paginas, idioma, formato, precio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.anio = anio
        self.genero = genero
        self.paginas = paginas
        self.idioma = idioma
        self.formato = formato
        self.precio = precio

        print(f"Titulo:{self.titulo}")
        print(f"Autor:{self.autor}")
        print(f"ISBN:{self.isbn}")
        print(f"Editorial:{self.editorial}")
        print(f"Año:{self.anio}")
        print(f"Género:{self.genero}")
        print(f"Páginas:{self.paginas}")
        print(f"Idioma:{self.idioma}")
        print(f"Formato:{self.formato}")
        print(f"Precio:{self.precio}")

    def leer (self): print("Iniciando lectura")
    def mostrar_informacion(self):
        print("Detalles del libro")
        print(f"'{self.titulo}' de {self.autor} (self.anio)")
        