def menu_longitud():
    print("\nSeleccione una opción:")
    print("1. Metros a kilómetros")
    print("2. Kilómetros a metros")
    opcion = input("Ingrese su elección: ")

    if opcion == '1':
        metros = float(input("Ingrese los metros: "))
        print(f"{metros} metros son {metroskilometros(metros)} kilómetros.")
    elif opcion == '2':
        kilometros = float(input("Ingrese los kilómetros: "))
        print(f"{kilometros} kilómetros son {kilometrosmetros(kilometros)} metros.")
    else:
        print("Opción no válida.")

def menu_masa():
    print("\nSeleccione una opción:")
    print("1. Gramos a kilogramos")
    print("2. Kilogramos a gramos")
    opcion = input("Ingrese su elección: ")

    if opcion == '1':
        gramos = float(input("Ingrese los gramos: "))
        print(f"{gramos} gramos son {gramoskilogramos(gramos)} kilogramos.")
    elif opcion == '2':
        kilogramos = float(input("Ingrese los kilogramos: "))
        print(f"{kilogramos} kilogramos son {kilogramosgramos(kilogramos)} gramos.")
    else:
        print("Opción no válida.")

def menu_temperatura():
    print("\nSeleccione una opción:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Ingrese su elección: ")

    if opcion == '1':
        celsius = float(input("Ingrese los grados Celsius: "))
        print(f"{celsius} grados Celsius son {celsiusfahrenheit(celsius)} grados Fahrenheit.")
    elif opcion == '2':
        fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
        print(f"{fahrenheit} grados Fahrenheit son {fahrenheitcelsius(fahrenheit)} grados Celsius.")
    else:
        print("Opción no válida.")

# Programa principal
while True:
   
    eleccion = input("Ingrese su elección: ")

    if eleccion == '1':
        menu_longitud()
    elif eleccion == '2':
        menu_masa()
    elif eleccion == '3':
        menu_temperatura()
    elif eleccion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")
        