def saludar():
    print("Bienvenido al menu de operaciones matematicas")
def suma_total(numbers):
    return sum(numbers)
def calcular_promedio (numbers):
    return sum(numbers)/len(numbers ) if numbers else 0
def contar_positivos_negativos(numbers):
    positivos = 0
    negativos = 0
    for number in numbers:
        if number > 0:
            positivos += 1
        elif number < 0:
            negativos += 1
    return positivos, negativos
def calcular_el_area_de_triangulo(base, altura):
    return base*altura/2
def calcular_si_numero_es_par_o_impar(number_):
    return number_ % 2 == 0
def calcular_promedio_notas(suma, cantidad):
    if cantidad != 0:
        resultado = suma/cantidad
    else:
        resultado = 0
    return resultado
def mostrar_el_numero_mayor_y_menor(mayor, menor):
    print("el numero mayor es: ", mayor)
    print("El numero menor es: ", menor)

saludar()
while True:
    print("\n ---MENU---")
    print("1. Ingresar n numeros y mostrar")
    print("2. Calcular el area de un triangulo")
    print("3. Verificar si un numero es par o impar")
    print("4. Calcular el promedio de n calificaciones")
    print("5. Ingresar n numeros y verificar cual es el mayor y menor de ellos")
    print("6. Salir")
    option = input("Elija una de las opciones (1-6) ")
    match option:
        case "1":
            number_user = int(input("Cuantos numeros desea ingresar "))
            numbers=[]
            for i in range(number_user):
                number = float(input("Ingrese los numneros "))
                numbers.append(number)
            positivos, negativos = contar_positivos_negativos(numbers)
            print("\n --Resultados--")
            print(f"La suma total es: {suma_total(numbers)}")
            print(f"El promedio de los numeros es: {calcular_promedio(numbers)}")
            print(f"la cantidad de numeros negativos son: {negativos}")
            print(f"la cantidad de numeros positivos son: {positivos}")
        case "2":
            print("\n --Calculo del area de un triangulo--")
            base = float(input("Ingrese la medida de la base "))
            altura = float(input("Ingrese la medida de la altura del triangulo "))
            print(f"El area del triangulo es: {calcular_el_area_de_triangulo(base,altura)}")
        case "3":
            print("\n --Numero par o impar--")
            number_ = int(input("Ingrese el numero que desea verificar "))
            if calcular_si_numero_es_par_o_impar(number_):
                print("El numero que Usted ingreso es par")
            else:
                print("El numero que Usted ingreso es impar")
        case "4":
            print("\n --Calculo de promedio de calificaciones--")
            calificacion = int(input("Ingrese el numero de calificaciones que se va a calcular "))
            adittion = 0
            for i in range(calificacion):
                notas= float(input("Ingrese sus notas "))
                adittion += notas
            print(f"El promedio de las calificaciones es: {calcular_promedio_notas(adittion, calificacion)}")
        case "5":
            print("\n --Mostrar el mayor y menor de los numeros ingresados")
            cantidad_numeros = int(input("Ingrese que cantidad de numeros va a ingresar "))
            if cantidad_numeros ==0:
                print("Debe ingresar un numero ")
            else :
                numero = float(input("Ingrese un numero "))
                mayor = numero
                menor = numero
                for i in range (1, cantidad_numeros):
                    numero = float(input("Ingrese un numero "))
                    if numero > mayor:
                        mayor=numero
                    if numero < menor:
                        menor=numero
                mostrar_el_numero_mayor_y_menor(mayor, menor)
        case "6":
            print("Gracias por usar el programa de operaciones matematicas")
            break
        case _:
            print("Usted ingreso un dato no valido, vuelva a intentarlo")