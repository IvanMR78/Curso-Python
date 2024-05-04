def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    while True:
        # usuario ingresa su nombre
        nombre = input("Por favor, ingresa tu nombre: ")
        
        #aqui valida que no este en blanco
        while nombre == "":
            print("Error: El nombre no puede estar vacío.")
            nombre = input("Por favor, ingresa tu nombre: ")

        # usuario ingresa su edad
        while True:
            try:
                edad = int(input("Por favor, ingresa tu edad: "))
                #aqui valida no este en blanco o que sea negativo 
                if edad <= 0:
                    print("Error: La edad debe ser un número entero positivo.")
                else:
                    break
            except ValueError:
                print("Error: Ingresa un número entero válido para la edad.")

        # usuario ingresa su peso en kilogramos
        while True:
            try:
                peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
                #aqui valida que no este en ceros o negatigo el peso
                if peso <= 0:
                    print("Error: El peso debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Error: Ingresa un número válido para el peso.")

        # Solicitar al usuario que ingrese su altura en metros
        while True:
            try:
                altura = float(input("Por favor, ingresa tu altura en metros(m.cm): "))
                if altura <= 0:
                    print("Error: La altura debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Error: Ingresa un número válido para la altura.")

        # aqui hace el calculo
        imc = calcular_imc(peso, altura)

        # aqui muestra todos los datos y resultado
        print("\n¡Hola, {}!".format(nombre))
        print("Tu índice de masa corporal es: {:.2f}".format(imc))

        # para repetir el proceso para un nuevo usuario
        respuesta = input("¿Deseas calcular el IMC para otro individuo? (s/n): ")
        if respuesta.lower() != 's':
            break

if __name__ == "__main__":
    main()