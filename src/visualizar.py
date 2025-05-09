from src.procesar_y_hashear import procesar_documentos_carpeta
from src.comparar_similitud import similitud_jaccard, merge_sort
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt
import os
topn = 0
def construir_grafo_top_similares(top_n=10):
    global topn
    topn = top_n
    tablas_hash = procesar_documentos_carpeta()
    G = nx.Graph()

    # Comparar todos los pares y calcular similitud
    pares_similares = []
    for doc1, doc2 in combinations(tablas_hash.keys(), 2):
        sim = similitud_jaccard(tablas_hash[doc1], tablas_hash[doc2])
        pares_similares.append((doc1, doc2, sim))

    # Ordenar por similitud descendente
    pares_top = merge_sort(pares_similares)[:top_n]

    # Agregar nodos y aristas al grafo
    for doc1, doc2, sim in pares_top:
        G.add_node(doc1)
        G.add_node(doc2)
        G.add_edge(doc1, doc2, weight=sim)

    return G, pares_top

def visualizar_grafo(G, pares_top, guardar_en_png=True):
    pos = nx.spring_layout(G, seed=42)

    # Nodos
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=600)
    nx.draw_networkx_labels(G, pos, font_size=8)

    # Aristas con pesos
    pesos = [G[u][v]['weight'] * 5 for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, width=pesos, alpha=0.7)

    # Etiquetas de peso
    etiquetas = { (u, v): f"{G[u][v]['weight']:.2f}" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas, font_size=6)

    plt.title(f"{topn} Documentos Más Similares")
    plt.axis('off')
    plt.tight_layout()

    if guardar_en_png:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resultados"))
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        nombre_base = "grafo"
        extension = ".png"
        contador = 0

        while True:
            if contador == 0:
                nombre_archivo = f"{nombre_base}{extension}"
            else:
                nombre_archivo = f"{nombre_base}({contador}){extension}"

            ruta_completa = os.path.join(base_path, nombre_archivo)
            if not os.path.exists(ruta_completa):
                break
            contador += 1

        # Save the graph image
        plt.savefig(ruta_completa, dpi=300)
        print(f"\n✅ Grafo guardado como imagen en: {ruta_completa}")

        # Generate the corresponding text file name
        nombre_archivo_txt = nombre_archivo.replace(extension, ".txt")
        ruta_completa_txt = os.path.join(base_path, nombre_archivo_txt)

        # Write the top pairs to the text file
        with open(ruta_completa_txt, "w", encoding="utf-8") as archivo:
            archivo.write(f"Top {topn} Documentos Más Similares:\n\n")
            for i, (doc1, doc2, sim) in enumerate(pares_top, 1):
                sim = sim * 100
                archivo.write(f"{i}. {doc1} <-> {doc2} => Similitud: {sim:.4f}%\n")

        print(f"\n✅ Resultados guardados en: {ruta_completa_txt}")
    plt.show()

    # También imprimir los pares en consola
    print("\n"f"{topn} pares más similares:")
    for i, (doc1, doc2, sim) in enumerate(pares_top, 1):
        sim = sim * 100
        print(f"{i}. {doc1} <-> {doc2} => Similitud: {sim:.4f}%")

    # Y escribir :)
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resultados"))
    nombre_base = f"{topn}_similares"

# Ejecutar si se corre directamente
if __name__ == '__main__':
    grafo, top10 = construir_grafo_top_similares(top_n=10)
    visualizar_grafo(grafo, top10)
