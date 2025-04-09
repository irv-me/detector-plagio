import os


from src import generador_archivos, procesar_y_hashear, visualizar, testeador


#== ARCHIVOS ==

#Quieres generar nuevos archivos?
NuevosArchivos = True

#En caso de querer usar uno de los tests, especifica la ruta del archivo
#Recuerda poner NuevosArchivos = False
Testear = False
#Nombre de la carpeta
Test = "MuchoTexto"
# == GRAFO ==
#Cuantas de las similitudes mas altas quieres ver?
Puestos = 10
#Quieres que se guarde la imagen y la informacion en un archivo?
GuardarGrafo = True


def main():
    if Testear: testeador.copiar_archivos_de_test(Test)
    if Testear: NuevosArchivos = False
    if NuevosArchivos: generador_archivos.generar_archivos_random(cantidad=100)
    grafo, top10 = visualizar.construir_grafo_top_similares(Puestos)
    visualizar.visualizar_grafo(grafo, top10, guardar_en_png=GuardarGrafo)






if __name__ == "__main__":
    main()