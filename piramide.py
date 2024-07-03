def generar_piramide(n):
     # Genera la pirámide de asteriscos centrada
    for i in range(n):
        espacios = n - i - 1
        asteriscos = 2 * i + 1
        print(' ' * espacios + '*' * asteriscos)

def main():
    while True:
        try:
            n = int(input("Ingrese un número entero mayor o igual a 1: "))
            if n >= 1:
                break
            else:
                print("El número debe ser mayor o igual a 1.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    generar_piramide(n)

if __name__ == "__main__":
    main()