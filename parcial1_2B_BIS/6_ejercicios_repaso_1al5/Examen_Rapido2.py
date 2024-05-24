def capturar_datos_alumno():
    nombre = input("Nombre del alumno: ")
    carrera = input("Carrera: ")
    parcial1 = float(input("Calificación del parcial 1: "))
    parcial2 = float(input("Calificación del parcial 2: "))
    parcial3 = float(input("Calificación del parcial 3: "))
    proyecto_final = float(input("Calificación del proyecto final: "))

    return {
        "nombre": nombre,
        "carrera": carrera,
        "parciales": [parcial1, parcial2, parcial3],
        "proyecto_final": proyecto_final
    }

def calcular_promedio_parciales(parciales):
    return sum(parciales) / len(parciales)

def main():
    alumnos = []
    while True:
        alumno = capturar_datos_alumno()
        alumnos.append(alumno)

        promedio_parciales = calcular_promedio_parciales(alumno["parciales"])
        calificacion_final = alumno["proyecto_final"]

        print(f"\nPromedio de parciales: {promedio_parciales:.2f}")
        print(f"Calificación final: {calificacion_final:.2f}")

        if calificacion_final < 80 or calificacion_final > 50:
            print("El alumno debe presentar extraordinario")

        respuesta = input("\n¿Deseas capturar otro alumno? (si/no): ")
        if respuesta.lower() != "si":
            break

    # Calculamos el promedio de calificaciones de todos los alumnos
    promedio_final_alumnos = sum(alumno["proyecto_final"] for alumno in alumnos) / len(alumnos)
    print(f"\nPromedio de calificaciones de todos los alumnos: {promedio_final_alumnos:.2f}")

if __name__ == "__main__":
    main()
