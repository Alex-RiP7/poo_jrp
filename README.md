# Repositorio de Programación Orientada a Objetos con Python
Repositorio con ejercicios de Programación Orientada a Objetos
markdown

## 1. Crear .gitignore

Crear el archivo .gitignore para configurar los archivos y carpetas no deseamos que se guarden en el repositorio

````shell
*.pyc
__pycache__/
````

## 2. Indexar archivos y carpetas

Indexa todos los directorios y carpetas en busca de documentos nuevos.

````shell
git add .
````

## 3. Crear un COMMIT

Crea un commit o punto de control de los cambios realizados en el proyecto.

````shell
git commit -m "CREATED .gitignore"
````

* CREATED - se crearon nuevas carpetas o archivos.
*UPDATED - Se actualizaron o agregaron nuevas funciones.
* FIXED - Se corrigieron errores.

## 4. Realizar el COMMIT

Sincroniza cambios realizados en el repositorio.

````shell
git push -u origin main
````

## 5. Agregar Documentación a los métodos

Agregar un **Docstring** a los métodos generados.

```python
    # 1. DEFINICIÓN METODODOS (Este metodo recibe 2 variables enteras, las suma y regresa el resultado de la suma)
    def metodoDos(self, variable_uno:int, variable_dos:float)->int:

        # 2. SECCIÓN 'ARGS' (Agregar un docstring documenta el método e indica qué valores necesita y de qué tipo deben ser.)
        Args:
        variable_uno:int - Primer numero entero
        variable_dos:int - Segundo numero entero

        # 3. SECCIÓN 'RETURN' (Es la parte de la documentación que explica qué valor o tipo de objeto devolverá la función al finalizar.)
        Return:
        suma : int - Suma de los dos numeros enteros
        
        # 4. OPERACIÓN LÓGICA (Aquí se suma la `variable_uno` y `variable_dos`, y el resultado se guarda en la variable local `suma`.)
        suma = variable_uno + variable_dos
        
        # 5. INSTRUCCIÓN RETURN (return devuelve el resultado de un método y int() lo convierte antes en un número entero.)
        return int(suma)