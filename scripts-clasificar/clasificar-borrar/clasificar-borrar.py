import os
import shutil

# Ruta de la carpeta que contiene los archivos JPEG
path_jpeg = "D:/PILAS ORIGIN - copia/PILAS ORIGIN MASTER/pequenos"

# Ruta de la carpeta en la que buscar y mover los archivos
path_move = "D:/PILAS ORIGIN MASTER CON COLOR PARA SEED/amarillo/New folder"

# Ruta de la carpeta en la que buscar y borrar los archivos
path_delete = "D:/PILAS ORIGIN MASTER CON COLOR PARA SEED/amarillo"

# Obtener lista de archivos JPEG
jpeg_files = [f for f in os.listdir(path_jpeg) if f.endswith('.jpeg') or f.endswith('.jpg')]

# Recorrer la lista de archivos JPEG y mover los archivos con el mismo nombre
for jpeg_file in jpeg_files:
    filename = os.path.splitext(jpeg_file)[0]  # obtener el nombre del archivo sin la extensión
    for file in os.listdir(path_move):
        if file.startswith(filename) and not (file.endswith('.jpeg') or file.endswith('.jpg')):
            # mover el archivo a la carpeta de destino
            shutil.move(os.path.join(path_move, file), os.path.join("D:/PILAS ORIGIN MASTER CON COLOR PARA SEED/amarillo pequenos", file))

# Obtener lista de archivos movidos
moved_files = [f for f in os.listdir("D:/PILAS ORIGIN MASTER CON COLOR PARA SEED/amarillo pequenos")]

# Obtener lista de archivos a borrar en la carpeta delete
delete_files = [f for f in moved_files if os.path.isfile(os.path.join(path_delete, f))]

# Creamos una lista vacía para almacenar los nombres de los archivos borrados
archivos_borrados = []

# Iteramos a través de los archivos a borrar
for archivo in delete_files:
    # Construimos la ruta completa del archivo en la carpeta delete
    ruta_archivo_delete = os.path.join(path_delete, archivo)
    # Verificamos si existe el archivo en la carpeta delete
    if os.path.isfile(ruta_archivo_delete):
        # Si existe, lo borramos
        os.remove(ruta_archivo_delete)
        # Agregamos el nombre del archivo a la lista de archivos borrados
        archivos_borrados.append(archivo)

# Creamos un archivo de texto con la lista de archivos borrados de la carpeta delete
with open("archivos_borrados.txt", "w") as archivos_borrados_txt:
    archivos_borrados_txt.write("\n".join(archivos_borrados))