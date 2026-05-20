from casa import Casa 
from silla import Silla
from mesa import Mesa
from universidad import Universidad
from telefono import Telefono
from libro_biblioteca import Libro
from transporte import Transporte
from perro import Perro
from p_videojuego import PersonajeVideojuego
from coche import Coche

if __name__ == "__main__":
    print("Prueba de todas las clases.")

    #  1. CASA 
    print("Prueba de Casa")
    mi_casa = Casa(
        direccion="Av. Revolución 456, Puebla",
        color="Blanco",
        numero_pisos=2,
        habitaciones=4,
        banos=3,
        area_construida=180,
        garage=True,
        jardin=True,
        anio_construccion=2022,
        precio="$3,200,000"
    )
    mi_casa.mostrar_informacion()

    #  2. SILLA 
    print("Prueba de Silla")
    silla_oficina = Silla(
        material="Madera y tela", color="Negro", altura=95, peso=8,
        tipo="Ejecutiva", respaldo="Alto", ruedas=True,
        capacidad_carga=150, precio="$2,800", fabricante="OfiMax"
    )
    silla_oficina.sentarse()

    #  3. MESA 
    print("Prueba de Mesa")
    mesa_comedor = Mesa(
        material="Madera", forma="Rectangular", longitud=180, ancho=90,
        altura=75, color="Café", capacidad_personas=6, peso=45,
        precio="$4,500", ubicacion="Comedor"
    )
    mesa_comedor.colocar_objetos()

    #  4. UNIVERSIDAD 
    print("Prueba de Universidad")
    utp = Universidad(
        nombre="Universidad Tecnológica de Puebla",
        localidad="Puebla, México",
        rector="Jesús Morales Rodríguez",
        carreras="20+ carreras técnicas y de ingeniería",
        alumnos=8500,
        campus="Zona Industrial Oriente",
        fundacion=2003,
        tipo="Pública Tecnológica",
        pagina_web="www.utpuebla.edu.mx",
        telefono="222 123 4567"
    )
    utp.inscribir_alumno()

    #  5. TELÉFONO 
    print("Prueba de Teléfono")
    mi_celular = Telefono(
        marca="Samsung", modelo="Galaxy S25", color="Negro",
        ram="16GB", almacenamiento="512GB", camara="200MP",
        bateria="5000mAh", sistema="Android 15", pantalla="6.8\"",
        precio="$28,999"
    )
    mi_celular.llamar()

    #  6. LIBRO 
    print("Prueba de Libro")
    libro = Libro(
        titulo="Python para Todos", autor="Raúl González",
        isbn="978-607-32-4567-8", editorial="Editorial UTP",
        anio=2025, genero="Programación", paginas=452,
        idioma="Español", formato="Físico", precio="$450"
    )
    libro.leer()

    #  7. TRANSPORTE 
    print("Prueba de Transporte")
    camion = Transporte(
        tipo="Camión de carga", capacidad=2, velocidad_max=110,
        combustible="Diesel", peso=8500, color="Rojo",
        longitud=12.5, fabricante="Freightliner",
        anio=2023, precio="$1,200,000"
    )
    camion.moverse()

    #  8. PERRO 
    print("Prueba de Perro")
    mi_perro = Perro(
        nombre="Max", raza="Pastor Alemán", edad=4, color="Negro y café",
        peso=32, altura=65, genero="Macho", temperamento="Leal y protector",
        vacunado=True, dueno="Juan Pérez"
    )
    mi_perro.ladrar()
    mi_perro.jugar()

    #  9. PERSONAJE DE VIDEOJUEGO
    print("Prueba de Personaje (Yasha)")
    yasha = PersonajeVideojuego(
        nombre="Yasha", juego="Asura's Wrath", raza="Semidiós",
        arma_principal="Espada de Mantra", poder_especial="Mantra Burst",
        color_cabello="Rojo", color_ojos="Dorados", altura=185,
        fuerza="Extremadamente alta", afinidad="Fuego y Viento"
    )
    yasha.atacar()
    yasha.usar_poder_especial()

    #  10. COCHE 
    print("Prueba de Coche")
    mi_coche = Coche(
        marca="Toyota", modelo="Corolla", color="Blanco",
        anio=2024, placas="XYZ-9876", numero_puertas=4,
        velocidad_max=180, combustible="Gasolina",
        kilometraje=8500, precio="$320,000"
    )
mi_coche.encender()
mi_coche.tocar_bocina()
