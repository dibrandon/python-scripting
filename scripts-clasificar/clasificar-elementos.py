import os
import shutil

# Ruta de la carpeta que contiene los archivos JPEG
path_jpeg = "D:/PILAS ORIGIN - copia/PILAS ORIGIN MASTER/pequenos"

# Ruta de la carpeta en la que buscar y mover los archivos
path_move = "D:/PILAS ORIGIN MASTER CON COLOR PARA SEED/amarillo/New folder 3"

# Obtener lista de archivos JPEG
jpeg_files = [f for f in os.listdir(path_jpeg) if f.endswith('.jpeg') or f.endswith('.jpg')]

# Recorrer la lista de archivos JPEG y mover los archivos con el mismo nombre
for jpeg_file in jpeg_files:
    filename = os.path.splitext(jpeg_file)[0]  # obtener el nombre del archivo sin la extensión
    for file in os.listdir(path_move):
        if file.startswith(filename) and not (file.endswith('.jpeg') or file.endswith('.jpg')):
            # mover el archivo a la carpeta de destino
            shutil.move(os.path.join(path_move, file), os.path.join("D:/PILAS ORIGIN MASTER CON COLOR PARA SEED/amarillo pequenos", file))