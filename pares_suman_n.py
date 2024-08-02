# Pregunta 2

from typing import List, Tuple

def pares_suman_n(n: int) -> List[Tuple[int, int]]:
    return [(i, n -i) for i in range(1, (n // 2) + 1)]

if __name__ == '__main__':
    # Ejemplo
    # Output [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]
    print(pares_suman_n(10))