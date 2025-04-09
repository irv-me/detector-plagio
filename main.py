import os


from src import generador_archivos, procesar_y_hashear, visualizar




#Quieres generar nuevos archivos?
NuevosArchivos = True

# == GRAFO ==
#Cuantas de las similitudes mas altas quieres ver?
Puestos = 2
#Quieres que se guarde imagen?
GuardarImagen = True


def main():
    # Generar archivos de texto aleatorios
    generador_archivos.generar_archivos_random(cantidad=100, ejecutar=NuevosArchivos)
    grafo, top10 = visualizar.construir_grafo_top_similares(Puestos)
    visualizar.visualizar_grafo(grafo, top10, guardar_en_png=GuardarImagen)






if __name__ == "__main__":
    main()