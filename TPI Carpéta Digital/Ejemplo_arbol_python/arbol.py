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
def mostrar_arbol(arbol, nivel=0):
    if arbol is not None:
        mostrar_arbol(arbol[2], nivel + 1)
        print('    ' * nivel + str(arbol[0]))
        mostrar_arbol(arbol[1], nivel + 1)

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


