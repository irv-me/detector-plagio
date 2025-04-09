import random

def generar_texto_random(num_palabras):

    palabras = [
        "casa de manolo", "fui a la", "pero un", "árbol", "sol", "luna", "aparecio", "cielo",
        "agua", "fuego", "y", "aire", "amigo", "al final", "lo que importa es",
        "trabajo", "amor", "felicidad", "tiempo", "vida"
    ]
    texto = " ".join(random.choice(palabras) for _ in range(num_palabras))
    return texto

def generar_archivos_random(cantidad=100):
    for i in range(1, cantidad + 1):
        num_palabras = random.randint(20, 100)
        contenido_random = generar_texto_random(num_palabras)
        nombre_archivo = f"documentos/archivo_{i}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido_random)


generar_archivos_random(100)