import convertidor

while True:
    opcion = convertidor.mostrar_menu()
    opcion = int(input("Elija: "))
    
    if opcion == 1:
        X = int(input("""1 para m a km
        2 para km a m
        :"""))
        if X == 1:
            metros = int(input("Ingresa cuantos metros convertir: "))
            print("Tienes {} km".format(convertidor.longitudmetros(metros))) 
        elif X == 2:
            kilometros = int(input("Ingresa cuantos km convertir: "))
            print("Tienes {} metros".format(convertidor.longitudkilometros(kilometros)))
    
    elif opcion == 2:
        X = int(input("""1 para g a kg
        2 para kg a g 
        :"""))
        if X == 1:
            gramos = int(input("Ingrese cuantos gramos convertir: "))
            print("Tienes {} kg".format(convertidor.masagramos(gramos)))
        elif X == 2:
            kilogramos = int(input("Ingrese cuantos kilogramos convertir: "))
            print("Tienes {} g".format(convertidor.masakilogramos(kilogramos)))
    
    elif opcion == 3:
        X = int(input("""1 para C° a F°
        2 para F° a C°
        :"""))
        if X == 1:
            celcius = int(input("Ingrese cuantos grados Celsius convertir: "))
            print("Tienes {} °F".format(convertidor.tiempocelcius(celcius)))
        elif X == 2:
            fahrenheit = int(input("Ingrese cuantos grados Fahrenheit convertir: "))
            print("Tienes {} °C".format(convertidor.tiempofahrenheit(fahrenheit)))
    
    elif opcion == 4:
        print("Saliendo...")
        break