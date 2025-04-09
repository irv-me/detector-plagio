import os
import re

# Función para limpiar y tokenizar el texto en n-gramas (por defecto, bi-gramas)
def obtener_ngrama(texto, n=2):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)  # Elimina puntuación
    palabras = texto.split()
    ngramas = [' '.join(palabras[i:i+n]) for i in range(len(palabras)-n+1)]
    return ngramas

# Función para hashear cada n-grama y guardarlos en una tabla hash (set)
def procesar_documento(ruta_archivo, n=2):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        ngramas = obtener_ngrama(texto, n)
        tabla_hash = set(hash(ng) for ng in ngramas)
    return tabla_hash

# Procesar todos los documentos en la carpeta 'documentos/'
def procesar_documentos_carpeta(carpeta=None, n=2):
    if carpeta is None:
        carpeta = os.path.join(os.path.dirname(__file__), '../documentos/')
    carpeta = os.path.abspath(carpeta)  # Convertir a ruta absoluta
    tablas_hash = {}  # Diccionario para almacenar los hashes de cada documento
    for nombre_archivo in os.listdir(carpeta):
        if nombre_archivo.endswith('.txt'):
            ruta = os.path.join(carpeta, nombre_archivo)
            tabla = procesar_documento(ruta, n)
            tablas_hash[nombre_archivo] = tabla
            print(f"[OK] {nombre_archivo} procesado. {len(tabla)} n-gramas hash.")
    return tablas_hash

# Ejecutar si se corre el archivo directamente
if __name__ == '__main__':
    tablas = procesar_documentos_carpeta()

