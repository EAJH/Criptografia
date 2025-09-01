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
        #cofactor = ((-1)**(columna)) * determinante(M)
        det += matriz[0][columna] * cofactor

    return det


# ----------- Cálculo de la adjunta de la matriz. Cofactores --------
def adjunta(matriz):

    n = len(matriz)

    adj = []

    if n == 1:
        return [[1]] # La adjunta de una matriz de 1x1 es 1

    # 1. Creamos una matriz de cofactores vacía que posteriormente se irá
    # llenando con los determinantes de los cofactores calculados
    matriz_cofactores = []
    for i in range(0,n):
        fila_vacia = []
        for j in range(0,n):
            fila_vacia.append(0)
        matriz_cofactores.append(fila_vacia)
            

    # 2. Recorremos la matriz elemento por elemento para calcular cada
    # cofactor
    for fila in range(0,n):
        for columna in range(0,n):
            # Hacemos el proceso de obtención del menor para cada elemento
            M = []
            for k in range(0,n):
                if k != fila:
                    fila_temporal = []
                    for l in range(0,n):
                        if l != columna:
                            fila_temporal.append(matriz[k][l])
                    M.append(fila_temporal)
            
            # Calcular el cofactor
            cofactor_valor = ((-1)**(fila+columna)) * determinante(M)

            # Insertamos el valor calculado en la matriz de cofactores vacía
            matriz_cofactores[fila][columna] = cofactor_valor
    
    # 3. Calculamos la matriz transpuesta de la matriz de cofactores
    # obtenida previamente
    adj = transpuesta(matriz_cofactores)
    return adj



# -------------- Cálculo de la transpuesta de una matriz ---------
def transpuesta(matriz):

    n = len(matriz)

    transp = []

    # 1. Invertimos filas por columnas y las insertamos en la matriz 
    # transpuesta
    for fila in range(0,n):
        fila_temporal = []
        for columna in range(0,n):
            fila_temporal.append(matriz[columna][fila])
        transp.append(fila_temporal)

    return transp



# ------------- Cálculo de la inversa de la matriz -------------
def inversa(matriz):

    n = len(matriz)
    inv = []

    # 1. Calculamos el determinante, si es cero, no hay inversa
    det = determinante(matriz)

    if det == 0:
        return ("La matriz no tiene inversa.\n")
    
    # 2. Si el determinante es diferente de cero, sí hay inversa

    # 2.1 Calculamos la adjunta transpuesta
    adj_transp = adjunta(matriz)

    # 2.2 MUltiplicamos 1/det por la adj_transp
    factor_multiplicativo_determinante = 1/det

    for fila in range(0,n):
        fila_inversa = []
        for columna in range(0,n):
            fila_inversa.append(round((factor_multiplicativo_determinante)*(adj_transp[fila][columna]),4))
        inv.append(fila_inversa)
    return inv


# ------------- Impresión de la matriz en formato bidimensional ---------
def imprimir_matriz(matriz):

    n = len(matriz)

    for fila in range(0,n):
        for columna in range(0,n):
            print(matriz[fila][columna], end=" ")
        print()


# -------------- Lectura de una matriz elemento por elemento -------------
def ingresar_matriz():
    n = int(input("Ingrese la longitud de la matriz cuadrada: "))
    matriz = []
    for i in range(0,n):
        fila_vacia = []
        for j in range(0,n):
            fila_vacia.append(0)
        matriz.append(fila_vacia)

    for fila in range(0,n):
        for columna in range(0,n):
            matriz[fila][columna] = int(input(f"Ingrese el elemento {fila},{columna} de la matriz: "))

    return matriz


# ----------- Ejecución del algoritmo -------------
'''
matriz = [[1,3,5,9,7,88],
          [1,3,1,7,88,12],
          [4,3,9,7,6,456],
          [5,2,0,9,6,7],
          [2,2,33,4,7,0],
          [44,6,23,1,22,4]]
'''
matriz = ingresar_matriz()
resultado = inversa(matriz)
print("\nLa inversa de la matriz es: \n")
imprimir_matriz(resultado)