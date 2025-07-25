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

while True:
    print("\n ---MENU---")
    print("1. Ingresar n numeros y mostrar")
    print("2. Calcular el area de un triangulo")
    print("3. Verificar si un numero es par o impar")
    print("4. Calcular el promedio de n calificaciones")
    print("5. Ingresar n numeros y verificar cual es el mayor y menor de ellos")
    print("6. Salir")
    option = input("Elija una de las opciones (1-6)")
    match option:
        case "1":
            number_user = int(input("Cuantos numeros desea ingresar"))
            numbers=[]
            for i in range(number_user):
                number = float(input("Ingrese los numneros"))
                numbers.append(number)
            positivos, negativos = contar_positivos_negativos(numbers)
            print("\n --Resultados--")
            print(f"La suma total es: {suma_total(numbers)}")
            print(f"El promedio de los numeros es: {calcular_promedio(numbers)}")
            print(f"la cantidad de numeros negativos son: {negativos}")
            print(f"la cantidad de numeros positivos son: {positivos}")
