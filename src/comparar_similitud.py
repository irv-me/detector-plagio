from procesar_y_hashear import procesar_documentos_carpeta
from itertools import combinations

# Paso 4: Calcular Similitud de Jaccard entre dos conjuntos
def similitud_jaccard(set1, set2):
    interseccion = len(set1 & set2)
    union = len(set1 | set2)
    return interseccion / union if union != 0 else 0

# Paso 5: Implementar Merge Sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i][2] > der[j][2]:  # Ordenar de mayor a menor similitud
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Paso 6: Comparar documentos y mostrar los más similares
def comparar_documentos_y_mostrar_top_n(n=10):
    tablas_hash = procesar_documentos_carpeta()
    pares_similares = []

    # Todas las combinaciones de pares sin repetir (A, B)
    for doc1, doc2 in combinations(tablas_hash.keys(), 2):
        sim = similitud_jaccard(tablas_hash[doc1], tablas_hash[doc2])
        pares_similares.append((doc1, doc2, sim))

    # Ordenar usando Merge Sort
    pares_ordenados = merge_sort(pares_similares)

    # Mostrar los N pares más similares
    print(f"\nTop {n} pares de documentos más similares:\n")
    for i, (doc1, doc2, sim) in enumerate(pares_ordenados[:n], 1):
        print(f"{i}. {doc1} <-> {doc2} => Similitud: {sim:.4f}")

# Ejecutar si se corre directamente
if __name__ == '__main__':
    comparar_documentos_y_mostrar_top_n(n=10)