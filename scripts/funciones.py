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

    resultado = ""
    resultado += f"Numero decimal: {numero}\n"
    resultado += f"Representación binario: {binary}\n"
    resultado += f"Representación en 8 bits: {byte_rep}\n"
    resultado += f"Representación hexadecimal: {hexadecimal}\n"
    
    return resultado

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

from pathlib import Path
import os
import mimetypes
import re

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