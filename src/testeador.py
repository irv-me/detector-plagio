import os
import shutil



def copiar_archivos_de_test(carpeta_origen):
    # Ruta base del proyecto
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # Ruta de la carpeta "test"
    ruta_test = os.path.join(base_path, "tests", carpeta_origen)
    
    # Ruta de la carpeta "documentos"
    ruta_documentos = os.path.join(base_path, "documentos")
    
    # Verificar si la carpeta de origen existe
    if not os.path.exists(ruta_test):
        print(f"❌ La carpeta '{carpeta_origen}' no existe en 'tests'.")
        return
    
    # Crear la carpeta "documentos" si no existe
    if not os.path.exists(ruta_documentos):
        os.makedirs(ruta_documentos)
    
    # Limpiar la carpeta "documentos" antes de copiar
    for archivo in os.listdir(ruta_documentos):
        archivo_path = os.path.join(ruta_documentos, archivo)
        if os.path.isfile(archivo_path):
            os.remove(archivo_path)
    
    # Copiar los archivos de la carpeta seleccionada a "documentos"
    for archivo in os.listdir(ruta_test):
        archivo_origen = os.path.join(ruta_test, archivo)
        archivo_destino = os.path.join(ruta_documentos, archivo)
        if os.path.isfile(archivo_origen):
            shutil.copy2(archivo_origen, archivo_destino)
    
    print(f"✅ Archivos de la carpeta '{carpeta_origen}' copiados a 'documentos'.")

# Ejemplo de uso
if __name__ == "__main__":
    carpeta = input("Ingresa el nombre de la carpeta dentro de 'tests': ")
    copiar_archivos_de_test(carpeta)