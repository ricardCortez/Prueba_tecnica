# Pregunta 1

from collections import Counter
from typing import List

def contar_numeros_matriz(matriz: List[List[int]]) -> List[int]:
    conteo = Counter(num for fila in matriz for num in fila)

    solo_una_vez = sum(1 for num in conteo.values() if num == 1)
    repetidos = sum(1 for num in conteo.values() if num > 1)

    return [solo_una_vez, repetidos]

if __name__ == '__main__':
    # Ejemplos
    # Output: [0, 1]
    print(contar_numeros_matriz([[2, 2], [2,2]]))

    # Output: [4, 2]
    print(contar_numeros_matriz([[2, 1, 3], [4, 5, 2], [6, 6, 6]]))
