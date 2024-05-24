def main():
    aprobados = 0
    reprobados = 0

    for i in range(1, 16):
        calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
        if 0 <= calificacion <= 10:
            if calificacion >= 6:
                aprobados += 1
            else:
                reprobados += 1
        else:
            print("La calificación debe estar entre 0 y 10. Inténtalo de nuevo.")

    print(f"Aprobados: {aprobados}")
    print(f"No aprobados: {reprobados}")

if __name__ == "__main__":
    main()
