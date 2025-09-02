# Práctica 6. Cifrado Hill - Matriz inversa por el método de la adjunta

**Integrantes:**
- López Reyes Alam  
- García Martínez Luis Eduardo  
- Juárez Herrera Erick Adrián  
- Hernández García Pilar Jaqueline
- Romero Domínguez Ricardo Damián
- Benitez Pérez Michelle Paulina  

**Fecha:** 28-08-25  

---

## Descripción breve

En esta práctica se implementó un programa que calculara la matriz inversa de
una matriz de entrada de longitud `n x n`, a través del método de la matriz
adjunta. El objetivo de este es observar como la complejidad dentro del cifrado
del algoritmo de Hill radica en la naturaleza propia de las matrices y sus operaciones. 


## Qué y cómo se logró

- Se creó una función específica que permitiera leer la longitud de la matriz
deseada y con base a esta, generarla automáticamente.
- Una vez que los elementos de la matriz han sido leídos se manda a llamar la 
función de `inversa(matriz)`que implementa el procedimiento matemático visto en clase:
  1. Calcular el determinante de la matriz a través de la función `determinante(matriz)`, si el determinante es igual a 0, la matriz ingresada no tiene inversa:
    1.1. La función `determinante(matriz)` considera los casos base para matrices
    de `1 x 1`, `2 x 2` y `n x n`. Para los primeros dos casos se aplica la 
    fórmula conocida directamente. Para matrices con longitudes mayores a 2, se 
    utiliza el método de cofactores usando como fila de expansión la primera de estas y haciendo los cálculos correspondientes para la obtención del menor
    `M()`. Finalmente, se calcula el cofactor para cada uno de los elementos de la
    fila de expansión obteniendo el determinante del menor previamente generado 
    usando recursividad, para así generar el valor del determinante multiplicando
    el elemento correspondiente de la matriz por el cofactor calculado con 
    anterioridad.

  2. Calcular la adjunta de la matriz a través de la función `adjunta(matriz)`. 
  Si la matriz es de longitud 1, la adjunta es 1, para matrices de mayor tamaño
  se genera una matriz de cofactores vacía que posteriormente se irá llenando a 
  través del cálculo de los distintos cofactores para cada elemento. Una vez que
  la matriz de cofactores está completa, se manda a llamar a la función de 
  `transpuesta(matriz)`la cual intercambia filas por columnas de la matriz de 
  cofactores, resultando esto en la matriz adjunta.

  3. Finalmente, se calcula cada uno de los elementos de la inversa de la matriz
  recorriendo la matriz adjunta transpuesta y multiplicando cada uno de estos por 
  el factor multiplicativo de `1 / determinante(matriz)`, para así poder imprimir
  en terminal la matriz inversa de la inicialmente ingresada.

---
