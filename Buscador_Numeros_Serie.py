import os
import re
import shutil
import datetime
import math
import time
from pathlib import Path

inicio = time.time()

ruta = 'C:\\DEV\\Proyectos\\Buscador_de_Numeros_de_Serie\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for a in archivos:
            resultado = buscar_numero(Path(carpeta,a), mi_patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())

def mostrar():
    i = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNº SERIE')
    print('-------\t\t\t--------')
    for a in archivos_encontrados: #
        print(f'{a}\t{numeros_encontrados[i]}')
        i += 1
    print('\n')
    print(f'Numeros encontrados: {len(numeros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crear_listas()
mostrar()

