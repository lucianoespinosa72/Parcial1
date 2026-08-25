from collections import deque
from list import List
from super_heroes_data import superheroes

# 1. Preparación: Clase Personaje
class Personaje:
    def __init__(self, data: dict):
        self.name = data.get("name")
        self.alias = data.get("alias")
        self.real_name = data.get("real_name")
        # El atributo se llama bio para coincidir con lo que espera list.py en filter_contain_on_bio
        self.bio = data.get("short_bio") 
        self.first_appearance = data.get("first_appearance")
        self.is_villain = data.get("is_villain")

    def __str__(self):
        # Representación en string para facilitar los print
        tipo = "Villano" if self.is_villain else "Superhéroe"
        return f"{self.name} ({self.real_name}) - {tipo} - {self.first_appearance}"

def main():
    # Instanciamos la clase List personalizada
    lista_personajes = List()

    # Convertimos los diccionarios y los agregamos a la lista
    for data in superheroes:
        personaje = Personaje(data)
        lista_personajes.append(personaje)

    # Configuramos los criterios de ordenamiento requeridos usando add_criterion
    lista_personajes.add_criterion("name", lambda p: p.name)
    # Algunos personajes tienen real_name como None, por lo que usamos or "" para evitar errores al ordenar
    lista_personajes.add_criterion("real_name", lambda p: p.real_name if p.real_name else "")
    lista_personajes.add_criterion("first_appearance", lambda p: p.first_appearance)

    # 1. Listado ordenado de manera ascendente por nombre
    print("1. Personajes ordenados por nombre:")
    lista_personajes.sort_by_criterion("name")
    lista_personajes.show()
    print("-" * 50)

    # 2. Determinar en qué posición están The Thing y Rocket Raccoon
    print("2. Posiciones de The Thing y Rocket Raccoon:")
    # El método search ordena automáticamente según el criterio provisto y retorna el índice
    idx_thing = lista_personajes.search("The Thing", "name")
    idx_rocket = lista_personajes.search("Rocket Raccoon", "name")
    print(f"The Thing se encuentra en el índice: {idx_thing}")
    print(f"Rocket Raccoon se encuentra en el índice: {idx_rocket}")
    print("-" * 50)

    # 3. Listar todos los villanos
    print("3. Listado de todos los villanos:")
    # Como List hereda de list, podemos iterarla directamente
    for p in lista_personajes:
        if p.is_villain:
            print(p)
    print("-" * 50)

    # 4. Villanos en una cola (deque) que aparecieron antes de 1980
    print("4. Villanos que aparecieron antes de 1980:")
    cola_villanos = deque()
    for p in lista_personajes:
        if p.is_villain:
            cola_villanos.append(p)
            
    # Procesamos la cola extrayendo sus elementos por la izquierda
    while cola_villanos:
        villano = cola_villanos.popleft()
        if villano.first_appearance < 1980:
            print(villano)
    print("-" * 50)

    # 5. Listar los superhéroes que comienzan con Bl, G, My, y W
    print("5. Superhéroes que comienzan con Bl, G, My, y W:")
    # Para asegurar que solo sean superhéroes (no villanos), filtramos primero en una List temporal
    lista_solo_heroes = List()
    for p in lista_personajes:
        if not p.is_villain:
            lista_solo_heroes.append(p)
    
    # filter_start_with ya incluye los print dentro de list.py y acepta tuplas de prefijos
    lista_solo_heroes.filter_start_with(("Bl", "G", "My", "W"))
    print("-" * 50)

    # 6. Listado de personajes ordenado por nombre real de manera ascendente
    print("6. Personajes ordenados por nombre real:")
    lista_personajes.sort_by_criterion("real_name")
    lista_personajes.show()
    print("-" * 50)

    # 7. Listado de superhéroes ordenados por fecha de aparición
    print("7. Superhéroes ordenados por fecha de aparición:")
    lista_personajes.sort_by_criterion("first_appearance")
    for p in lista_personajes:
        if not p.is_villain:
            print(p)
    print("-" * 50)

    # 8. Buscar a Ant Man y modificar su nombre real a Scott Lang
    print("8. Modificación del nombre real de Ant Man:")
    idx_ant_man = lista_personajes.search("Ant Man", "name")
    if idx_ant_man is not None:
        lista_personajes[idx_ant_man].real_name = "Scott Lang"
        print(f"Modificado correctamente: {lista_personajes[idx_ant_man]}")
    else:
        print("Ant Man no fue encontrado.")
    print("-" * 50)

    # 9. Mostrar personajes con "time-traveling" o "suit" en la biografía
    print("9. Personajes con 'time-traveling' o 'suit' en su biografía:")
    # Debemos pasar los valores en minúscula ya que filter_contain_on_bio usa .lower()
    lista_personajes.filter_contain_on_bio(("time-traveling", "suit"))
    print("-" * 50)

    # 10. Eliminar a Electro y Baron Zemo y mostrar su información
    print("10. Eliminación de Electro y Baron Zemo:")
    # delete_value utiliza internamente el método search por lo que requiere el criterion
    eliminado_electro = lista_personajes.delete_value("Electro", criterion="name")
    if eliminado_electro:
        print(f"Electro fue eliminado. Información: {eliminado_electro}")
    else:
        print("Electro no se encontraba en la lista.")

    eliminado_zemo = lista_personajes.delete_value("Baron Zemo", criterion="name")
    if eliminado_zemo:
        print(f"Baron Zemo fue eliminado. Información: {eliminado_zemo}")
    else:
        print("Baron Zemo no se encontraba en la lista.")

if __name__ == "__main__":
    main()
