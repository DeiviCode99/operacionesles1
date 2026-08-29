def ascii_table(texto):
    print("Carácter     Decimal     Hexadecimal     Binario")
    print("---------------------------------------------------")
    for i in range(len(texto)):
        letter = texto[0+i]
        decimal_letter = ord(letter)
        hex_letter = format(decimal_letter, 'x')
        binary_letter = format(decimal_letter, 'b')
        print(f"{letter}            {decimal_letter}            {hex_letter}            {binary_letter}")


    print("\n")
    # Tamaño del archivo
    bytes_texto = len(texto.encode('UTF-8'))
    print(f"Tamaño en bytes del archivo es: {bytes_texto}")
    print(f"Tamaño en bits del aarchivo: {bytes_texto * len(texto)*2}")
    return

resultados = ascii_table("Colombia ")