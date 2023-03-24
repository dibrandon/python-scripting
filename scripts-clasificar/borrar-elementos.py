import os

# Definimos las rutas de las carpetas a usar
carpeta1 = "poner ruta antes de usar"
carpeta2 = "poner ruta antes de usar"

# Obtenemos la lista de archivos de la primera carpeta
archivos1 = os.listdir(carpeta1)

# Creamos una lista vacía para almacenar los nombres de los archivos borrados
archivos_borrados = []

# Iteramos a través de los archivos de la primera carpeta
for archivo in archivos1:
    # Construimos la ruta completa del archivo en la segunda carpeta
    ruta_archivo2 = os.path.join(carpeta2, archivo)
    # Verificamos si existe el archivo en la segunda carpeta
    if os.path.isfile(ruta_archivo2):
        # Si existe, lo borramos
        os.remove(ruta_archivo2)
        # Agregamos el nombre del archivo a la lista de archivos borrados
        archivos_borrados.append(archivo)

# Creamos un archivo de texto con la lista de archivos de la primera carpeta
with open("archivos1.txt", "w") as archivo1_txt:
    archivo1_txt.write("\n".join(archivos1))

# Creamos un archivo de texto con la lista de archivos borrados de la segunda carpeta
with open("archivos_borrados.txt", "w") as archivos_borrados_txt:
    archivos_borrados_txt.write("\n".join(archivos_borrados))