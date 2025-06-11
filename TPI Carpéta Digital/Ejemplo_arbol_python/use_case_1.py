"""
    Trabajo Practico Integrador de Programación 1
    
    Universidad Tecnológica Nacional

    Profesor: Julieta Trapé
    Materia: Programación 1
    Carrera: Tecnicatura Universitaria en Programación
    Tema: Árboles Binarios
    Módulo: Caso de uso 1 - Creación y recorrido de un árbol binario utilizando letras del alfabeto
    Integrantes:
    - Nombre 1: Manuel Galarza
    - Nombre 2: Gabriel Etchegoyen
    
    Fecha: 28/05/2025
    Descripción: Este script implementa un árbol binario en Python y realiza recorridos inorden, preorden y postorden.
"""

from arbol import crear_nodo, inorden, preorden, postorden, mostrar_arbol, imprimir_jerarquia_nivel


if __name__ == "__main__":
    # Ejecutar el caso de uso
    # Crear un árbol binario de ejemplo
    arbol = crear_nodo('A', crear_nodo('B', crear_nodo('D'), crear_nodo('E')), crear_nodo('C', None, crear_nodo('F')))
    # Mostrar visualización del árbol
    print("Árbol binario:")
    mostrar_arbol(arbol)

    #Jerarquia en el árbol
    print("\nJerarquía por niveles:")
    imprimir_jerarquia_nivel(arbol)

    # Recorridos
    print("\nRecorrido inorden:")
    inorden(arbol)

    print("\nRecorrido preorden:")
    preorden(arbol)

    print("\nRecorrido postorden:")
    postorden(arbol)

