"""
    Trabajo Practico Integrador de Programación 1
    
    Universidad Tecnológica Nacional

    Profesor: Julieta Trapé
    Materia: Programación 1
    Carrera: Tecnicatura Universitaria en Programación
    Tema: Árboles Binarios
    Módulo: Creación y recorrido de un árbol binario
    Integrantes:
    - Nombre 1: Manuel Galarza
    - Nombre 2: Gabriel Etchegoyen
    
    Fecha: 28/05/2025
    Descripción: Este script implementa un árbol binario en Python y realiza recorridos inorden, preorden y postorden.
"""


# Crear nodo del árbol
def crear_nodo(valor, izquierdo=None, derecho=None):
    return [valor, izquierdo, derecho]

# Insertar valor en ABB
def insertar(arbol, valor):
    if arbol is None:
        return crear_nodo(valor)
    if valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)
    else:
        arbol[2] = insertar(arbol[2], valor)
    return arbol

# Buscar valor en el árbol (retorna True o False)
def buscar(arbol, valor):
    if arbol is None:
        return False
    if valor == arbol[0]:
        return True
    elif valor < arbol[0]:
        return buscar(arbol[1], valor)
    else:
        return buscar(arbol[2], valor)

# Recorridos
def inorden(arbol):
    if arbol is not None:
        inorden(arbol[1])
        print(arbol[0], end=' ')
        inorden(arbol[2])

def preorden(arbol):
    if arbol is not None:
        print(arbol[0], end=' ')
        preorden(arbol[1])
        preorden(arbol[2])

def postorden(arbol):
    if arbol is not None:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0], end=' ')

# Mostrar árbol visualmente
def mostrar_arbol(arbol, prefijo='', es_izquierdo=True):
    if arbol is not None:
        mostrar_arbol(arbol[2], prefijo + ('│   ' if es_izquierdo else '    '), False)

        print(prefijo + ('└── ' if es_izquierdo else '┌── ') + str(arbol[0]))

        mostrar_arbol(arbol[1], prefijo + ('    ' if es_izquierdo else '│   '), True)

# Jerarquia en el árbol
def imprimir_jerarquia_nivel(arbol):
    from collections import deque
    if not arbol:
        return
    cola = deque()
    cola.append(arbol)
    while cola:
        nivel = len(cola)
        linea = []
        for _ in range(nivel):
            nodo = cola.popleft()
            if nodo:
                linea.append(str(nodo[0]))
                cola.append(nodo[1])
                cola.append(nodo[2])
        if linea:
            print("  ".join(linea))

# Menú interactivo
def menu():
    print("\nÁrbol Binario de Búsqueda (ABB) usando listas")
    print("1. Insertar un valor")
    print("2. Mostrar recorrido Inorden")
    print("3. Mostrar recorrido Preorden")
    print("4. Mostrar recorrido Postorden")
    print("5. Buscar un valor")
    print("6. Salir")

def main():
    arbol = None  # árbol vacío
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            try:
                val = int(input("Ingrese un número para insertar: "))
                arbol = insertar(arbol, val)
                print(f"Valor {val} insertado.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        elif opcion == '2':
            print("Árbol binario:")
            mostrar_arbol(arbol)
            print("Recorrido Inorden: ", end='')
            inorden(arbol)
            print()
        
        elif opcion == '3':
            print("Árbol binario:")
            mostrar_arbol(arbol)
            print("Recorrido Preorden: ", end='')
            preorden(arbol)
            print()
        
        elif opcion == '4':
            print("Árbol binario:")
            mostrar_arbol(arbol)
            print("Recorrido Postorden: ", end='')
            postorden(arbol)
            print()
        
        elif opcion == '5':
            try:
                val = int(input("Ingrese un número para buscar: "))
                encontrado = buscar(arbol, val)
                if encontrado:
                    print(f"El valor {val} está en el árbol.")
                else:
                    print(f"El valor {val} NO está en el árbol.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
