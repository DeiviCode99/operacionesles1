from pathlib import Path
import os
import mimetypes
import re

"""
Conversión de binario a decimal y hexadecimal
y representación de números en complemento a 2
"""

def complemento_a_1(binario_texto):
    inverso = ""
    for bit in binario_texto:
        if bit == "0":
            inverso += "1"
        else:
            inverso += "0"
    return inverso

def representacion_comp_dos(num):
    resultado = ""
    resultado += f"numero decimal: {num}\n"

    decimalplus = abs(num)
    binario = format(decimalplus, "b")
    resultado += f"numero positivo: {decimalplus}\n"
    resultado += f"numero binario: {binario}\n"

    copm_1 = complemento_a_1(binario)
    resultado += f"complemento a 1: {copm_1}\n"

    comp_1_decimal = int(copm_1, 2)
    comp_1_plus_1 = comp_1_decimal + 1
    binario_2 = format(comp_1_plus_1, "b")
    resultado += f"complemento a 2: {binario_2}\n"

    return resultado

def convert_to_binary(num):

    if num >= 0:
        # Conversión a binario
        numero = num
        binary = format(numero, 'b')
        hexadecimal = format(numero, 'x')

        # Representación de 8 bits
        num_digits = len(binary)
        if num_digits < 8:
            byte_rep = binary.zfill(8)
        else:
            byte_rep = binary

        resultado = ""
        resultado += f"Numero decimal: {numero}\n"
        resultado += f"Representación binario: {binary}\n"
        resultado += f"Representación en 8 bits: {byte_rep}\n"
        resultado += f"Representación hexadecimal: {hexadecimal}\n"
        
        return resultado
    else:
        return representacion_comp_dos(num)

"""
Representación de un texto en formato ASCII, decimal, hexadecimal y binario
"""

def ascii_table(texto):
    resultado = "Carácter     Decimal     Hexadecimal     Binario\n"
    resultado += "---------------------------------------------------\n"
    for i in range(len(texto)):
        letter = texto[i]
        decimal_letter = ord(letter)
        hex_letter = format(decimal_letter, 'x')
        binary_letter = format(decimal_letter, 'b')
        resultado += f"{letter}            {decimal_letter}            {hex_letter}            {binary_letter}\n"


    resultado += "\n"
    # Tamaño del archivo
    bytes_texto = len(texto.encode('UTF-8'))
    resultado += f"Tamano en bytes del archivo es: {bytes_texto}\n"
    resultado += f"Tamanio en bits del archivo: {bytes_texto * 8}\n"
    return resultado

"""Analisis de archivos binarios y detección de tipo de archivo a partir de su firma binaria"""
def archive_analisis(ruta):
    doc_name = Path(ruta).name
    bytes_size = os.path.getsize(ruta)
    type_doc, _ = mimetypes.guess_type(ruta)

    with open(ruta, 'rb') as f:
        first_bytes = f.read(8)
    
    hex_firm = first_bytes.hex()
    hex_firm = " ".join(re.findall(r".{1,2}", hex_firm))
    
    # Convertir firma hexadecimal a binario
    bin_firm = ""
    for byte in first_bytes:
        bin_firm += format(byte, '08b') + " "
    bin_firm = bin_firm.strip()

    resultado = ""
    resultado += f"Analizando archivo: {doc_name}\n"
    resultado += f"Tamano:\n{bytes_size} bytes\n"
    resultado += f"Tipo detectado:\n{type_doc if type_doc else 'Desconocido'}\n"
    resultado += f"Primeros bytes en hexadecimal:\n{hex_firm.upper()}\n"
    resultado += f"Firma hexadecimal convertida a binario:\n{bin_firm}\n"

    return resultado

"""
Detección de tipo de archivo a partir de su firma binaria
"""

def detective(ruta):
    doc_name = Path(ruta).name
    doc_name = doc_name.split('.')[0]
    bytes_size = os.path.getsize(ruta)
    type_doc, _ = mimetypes.guess_type(ruta)

    with open(ruta, 'rb') as f:
        firts_bytes = f.read(8)

    hex_firm = firts_bytes.hex()
    hex_firm = " ".join(re.findall(r".{1,2}", hex_firm))

    description = ""
    hipotesis = ""

    if firts_bytes.startswith(b'%PDF'):
        type_doc = "PDF"
        description = "Los primeros bytes coinciden con la firma característica de un archivo en formato PDF."
        hipotesis = "El archivo podría contener texto."
    elif firts_bytes.startswith(b'\x89PNG\r\n\x1a\n'):
        type_doc = "PNG"
        description = "Los primeros bytes coinciden con la firma característica de un archivo en formato PNG."
        hipotesis = "El archivo podría contener una imagen."
    elif firts_bytes.startswith(b'\xff\xd8\xff'):
        type_doc = "JPEG/JPG"
        description = "Los primeros bytes coinciden con la firma característica de un archivo en formato PNG."
        hipotesis = "El archivo podría contener una imagen."
    elif firts_bytes.startswith(b'MZ'):
        type_doc = "EXE/DLL"
        description = "Los primeros bytes coinciden con la firma característica de un archivo en formato EXE/DLL."
        hipotesis = "El archivo podría contener un ejecutable."
    elif firts_bytes.startswith(b'PK\x03\x04'):
        type_doc = "ZIP"
        description = "Los primeros bytes coinciden con la firma característica de un archivo en formato ZIP."
        hipotesis = "El archivo podría contener una archivo comprimido."
    elif firts_bytes.startswith(b'ID3') or firts_bytes.startswith(b'\xff\xfb'):
        type_doc = "MP3"
        description = "Los primeros bytes coinciden con la firma característica de un archivo en formato MP3."
        hipotesis = "El archivo podría contener un audio."
    elif firts_bytes.startswith(b'GIF87a') or firts_bytes.startswith(b'GIF89a'):
        type_doc = "GIF"
        description = "Los primeros bytes coinciden con la firma característica de un archivo en formato GIF."
        hipotesis = "El archivo podría contener una imagen animada."
    elif firts_bytes.startswith(b'\x7fELF'):
        type_doc = "ELF"
        description = "Los primeros bytes coinciden con la firma característica de un archivo en formato ELF."
        hipotesis = "El archivo podría contener un ejecutable de Linux."
    else:
        # Si no coincide con ninguna firma binaria conocida, intentamos ver si es texto plano
        try:
            with open(ruta, 'r', encoding='utf-8') as f_texto:
                f_texto.read(100)
            type_doc = "Texto Plano (.txt / .csv / código)"
        except UnicodeDecodeError:
            type_doc = "Binario Desconocido o Datos Propietarios (.dat puro)"

    resultado = ""
    resultado += f"Analizando archivo: {doc_name}.dat\n"
    resultado += f"Tamaño:\n{bytes_size} bytes\n"
    resultado += f"Tipo detectado:\n.{type_doc}\n"
    resultado += f"Primeros bytes en hexadcimal:\n{hex_firm.upper()}\n"
    resultado += f"EVIDENCIA ENCONTRADA:\n{description}\n"
    resultado +=f"HIPÓTESIS:\n{hipotesis}\n"
    resultado += f"VERIFICACIÓN:\nLa extensión original fue .dat pero el analisis de cu contenido indica que corresponde a una imagen{type_doc}"

    return resultado