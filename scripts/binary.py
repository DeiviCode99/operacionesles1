def convert_to_binary(num):

    # Conversión a binario
    numero = num
    binary = format(numero, 'b')

    # Representación de 8 bits
    num_digits = len(binary)
    if num_digits < 8:
        byte_rep = binary.zfill(8)
    else:
        byte_rep = binary

    # Representación hexadecimal
    hexadecimal = format(numero, 'x')

    print(f"Numero decimal: {numero}")
    print(f"Representeanción binario: {binary}")
    print(f"Representación en 8 bits: {byte_rep}")
    print(f"Representación hexadecimal: {hexadecimal}")
    
    return

resultados = convert_to_binary(14)
print(resultados)