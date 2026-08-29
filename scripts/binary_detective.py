from pathlib import Path
import os
import mimetypes
import re

def detective(ruta: str | Path):
    doc_name = Path(ruta).name
    doc_name = doc_name.split('.')[0]
    bytes_size = os.path.getsize(ruta)
    type_doc, _ = mimetypes.guess_type(ruta)

    with open(ruta, 'rb') as f:
        firts_bytes = f.read(8)

    hex_firm = firts_bytes.hex()
    hex_firm = " ".join(re.findall(r".{1,2}", hex_firm))

    # 3. Detectar el tipo real comparando los Magic Numbers
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

    print(f"Analizando archivo: {doc_name}.dat\n")
    print(f"Tamaño:\n{bytes_size} bytes\n")
    print(f"Tipo detectado:\n.{type_doc}\n")
    print(f"Primeros bytes en hexadcimal:\n{hex_firm.upper()}\n")
    print(f"EVIDENCIA ENCONTRADA:\n{description}\n")
    print(f"HIPÓTESIS:\n{hipotesis}\n")
    print(f"VERIFICACIÓN:\nLa extensión original fue .dat pero el analisis de cu contenido indica que corresponde a una imagen{type_doc}")
    return

resultado = detective(ruta="IchigoKurosakiBleach.dat")