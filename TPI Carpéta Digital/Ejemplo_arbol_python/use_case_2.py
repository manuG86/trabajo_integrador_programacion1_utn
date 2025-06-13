"""
    Trabajo Practico Integrador de Programación 1
    
    Universidad Tecnológica Nacional

    Profesor: Julieta Trapé
    Materia: Programación 1
    Carrera: Tecnicatura Universitaria en Programación
    Tema: Árboles Binarios
    Módulo: Caso de uso 2 - Creación y recorrido de un árbol binario utilizando puestos de una empresa
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
    arbol = crear_nodo("Director",crear_nodo("Jefe de Ventas", crear_nodo("Vendedor 1"), crear_nodo("Vendedor 2")),
    crear_nodo("Jefe de Producción",
        crear_nodo("Operario 1"),
        crear_nodo("Operario 2")
    )
)
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