print("=============================")
print("     MI CALCULADORA")
print("=============================")

while True:
    print("")
    print("¿Qué operación deseas realizar?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. División")
    print("5. Salir")
    print("----------------------------")

    opcion = input("Elige una opción: ")

    if opcion == "1":
    num1 = input("Ingresa el primer número")
    num1 = int(num1)
    num2 = input("Ingresa el segundo número")
