"""
    Trabajo Practico Integrador de Programación 1
    
    Universidad Tecnológica Nacional

    Profesor: Julieta Trapé
    Materia: Programación 1
    Carrera: Tecnicatura Universitaria en Programación
    Tema: Árboles Binarios
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

# Crear un árbol binario de ejemplo

arbol = crear_nodo('A', crear_nodo('B', crear_nodo('D'), crear_nodo('E')), crear_nodo('C', None, crear_nodo('F')))

# Mostrar visualización del árbol
print("Árbol binario:")
mostrar_arbol(arbol)

# Recorridos
print("\nRecorrido inorden:")
inorden(arbol)

print("\nRecorrido preorden:")
preorden(arbol)

print("\nRecorrido postorden:")
postorden(arbol)

