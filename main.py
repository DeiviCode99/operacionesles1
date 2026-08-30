from scripts import funciones

def main():
    print("---------- BIENVENIDO A BINARY REPRESENTATION ----------\n1. Decimal to Binary\n2. Text to ASCII code\n3. Document Analisis\n4. Binary Detective")
    
    while True:

        option = input("Ingrese la opción que desea usar: \n")

        if  option == "1":
            numero = int(input("Ingrese el numero que desea convertir en formato base 10: "))
            print(f"{funciones.convert_to_binary(numero)}\n")
        elif option == "2":
            texto = input("Ingrese el texto que desea representar en formato ASCII: ")
            print(f"{funciones.ascii_table(texto)}\n")
        elif option == "3":
            ruta = input("Ingrese la ruta del documento que desea analizar: ")
        elif option == "4":
            print("---------- BINARY DETECTIVE ACTIVATE ----------")
            print(f"{funciones.detective()}\n")
        else:
            print(f"{option} no es una opción valida, ingrese una de las opciones del menú.\n")


if __name__ == "__main__":
    main()