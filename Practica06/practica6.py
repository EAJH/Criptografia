'''
Objetivo: Generar un programa que calcule la inversa de una matriz
de la máximo que se pueda

1  2  3
4  5  6
7  8  9

'''

# ----------- Cálculo determinante por cofactores ----------
def determinante(matriz):

    n = len(matriz)

    # 1. Caso 1: La matriz es de 1x1
    if n == 1:
        return matriz[0][0]

    # 2. Caso 2: La matriz es de 2x2
    if n == 2:
        return ((matriz[0][0]*matriz[1][1]) - (matriz[0][1]*matriz[1][0]))

    # 3. Caso 3: La matriz es de 3x3 o superior
    det = 0

    # Tomamos como fila de expansión la primera 
    for columna in range(0,n):
        # Hacemos el proceso de obtención del menor
        M = []
        for fila in range(1,n):
            fila_temporal = []
            for k in range(0,n):
                if k != columna:
                    fila_temporal.append(matriz[fila][k])
            M.append(fila_temporal)
        
        # Cálculo del cofactor
        cofactor = ((-1)**(1+columna+1)) * determinante(M)
        det += matriz[0][columna] * cofactor

    return det


matriz = [[2,3,6],
          [8,1,2],
          [2,4,5]]
resultado = determinante(matriz)
print("El determinante es: ", resultado)