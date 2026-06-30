# -*- coding: utf-8 -*-
"""
Ejercicio 1: Funciones recursivas para búsqueda y listado de superhéroes.
"""

def buscar_capitan_america(lista, indice=0):
    """
    Busca recursivamente si "Capitán América" (o "Capitan America") 
    se encuentra en la lista.
    
    Caso Base:
    - Si el índice alcanza la longitud de la lista, significa que recorrimos
      toda la lista sin encontrar al personaje. Retorna False.
    - Si el elemento en el índice actual coincide con "Capitán América" 
      o "Capitan America" (ignorando mayúsculas/minúsculas y espacios),
      retorna True.
      
    Caso Recursivo:
    - Si no se cumple ningún caso base, llamamos a la función incrementando
      el índice en 1 para verificar el siguiente elemento.
    """
    # Caso Base 1: Fin de la lista alcanzado
    if indice >= len(lista):
        return False
    
    # Normalización para comparar sin importar mayúsculas o acentos simples
    nombre_actual = lista[indice].strip().lower()
    
    # Caso Base 2: Coincidencia encontrada
    if nombre_actual in ["capitán américa", "capitan america"]:
        return True
    
    # Caso Recursivo: Buscar en la siguiente posición
    return buscar_capitan_america(lista, indice + 1)


def listar_superheroes(lista, indice=0):
    """
    Recorre recursivamente la lista e imprime en pantalla el nombre
    de cada superhéroe.
    
    Caso Base:
    - Si el índice alcanza la longitud de la lista, terminamos la recursión.
      
    Caso Recursivo:
    - Imprime el superhéroe en la posición actual y luego se llama a sí misma
      con el índice incrementado en 1 para procesar el resto de la lista.
    """
    # Caso Base: Fin de la lista alcanzado, se detiene la recursión
    if indice >= len(lista):
        return
    
    # Imprimir el superhéroe actual
    print(f"- {lista[indice]}")
    
    # Caso Recursivo: Llamar para el siguiente índice
    listar_superheroes(lista, indice + 1)


# --- Bloque de Prueba ---
if __name__ == "__main__":
    # Lista de ejemplo con 15 superhéroes (incluyendo a Capitán América)
    superheroes = [
        "Star-Lord",
        "Deadpool",
        "Wolverine",
        "Ant-Man",
        "Scarlet Witch",
        "Captain Marvel",
        "Doctor Strange",
        "Black Panther",
        "Hawkeye",
        "Capitán América",
        "Black Widow",
        "Hulk",
        "Thor",
        "Spider-Man",
        "Iron Man"
    ]

    print("=== Listado de Superheroes ===")
    listar_superheroes(superheroes)
    print()

    # Ejecutar la búsqueda
    encontrado = buscar_capitan_america(superheroes)
    print(f"Esta Capitan America en la lista?: {encontrado}")


