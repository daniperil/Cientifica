##
import numpy as np
import heapq as pq


def fibonacci(n):
    n = n**2 - 1
    answer = []
    fib_0 = 1
    fib_1 = 1
    answer.append(fib_0)
    answer.append(fib_1)
    while n != 2:
        fib_i = fib_0+fib_1
        answer.append(fib_i)
        fib_0 = fib_1
        fib_1 = fib_i
        n -= 1
    answer.append(-1)
    return answer


def primos(n):
    arrayLength = 1
    maxToCheck = 1
    if n == 3:
        arrayLength = 20
        maxToCheck = 5
    elif n == 4:
        arrayLength = 50
        maxToCheck = 8
    else:
        arrayLength = 90
        maxToCheck = 10
    array = np.ones(arrayLength, dtype=int)
    array[0] = -1
    i = 1
    answer = []
    maxSaved = i
    while i <= maxToCheck:
        k = i+1
        if array[i] == -1:
            i += 1
            continue
        maxSaved = k
        answer.append(k)
        multiples = 2*k
        while multiples <= arrayLength:
            array[multiples-1] = -1
            multiples += k
        i += 1
    maxSaved += 1
    while maxSaved < arrayLength:
        if array[maxSaved - 1] == 1:
            answer.append(maxSaved)
        maxSaved += 1
    answer.append(-1)
    return answer


def pares(n):
    n = n**2 - 1
    answer = []
    add = 2
    answer.append(add)
    while n != 1:
        add += 2
        answer.append(add)
        n -= 1
    answer.append(-1)
    return answer


def impares(n):
    n = n**2 - 1
    answer = []
    add = 1
    answer.append(add)
    while n != 1:
        add += 2
        answer.append(add)
        n -= 1
    answer.append(-1)
    return answer


def potenciasDeDos(n):
    n = n**2 - 1
    answer = []
    i = n
    while n - i != n:
        add = 2**(n-i)
        answer.append(add)
        i -= 1
    answer.append(-1)
    return answer


def cuadratica(n):
    n = n**2 - 1
    answer = []
    i = 1
    while i != n+1:
        answer.append(i**2)
        i += 1
    answer.append(-1)
    return answer


def arregloAMatriz(arr, n):
    matriz = []
    for i in range(0, n):
        l = n * i
        add = []
        for j in range(0, n):
            l = n * i + j
            add.append(arr[l])
        matriz.append(add)
    return matriz


class Node:
    def __init__(self, inicial, padre, nivel, x, y, nuevoX, nuevoY):
        self.padre = padre
        self.matriz = inicial
        self.matriz[x][y] = self.matriz[nuevoX][nuevoY]
        self.matriz[nuevoX][nuevoY] = -1
        self.costo = 100000000
        self.x = nuevoX
        self.y = nuevoY
        self.nivel = nivel

    def __lt__(self, other):
        return self.costo+self.nivel < other.costo + other.nivel


def calcularCosto(inicial, final, n):
    costo = 0
    for i in range(n):
        for j in range(n):
            if inicial[i][j] != final[i][j]:
                costo += 1

    return costo


fila = [1, 0, -1, 0]
columna = [0, -1, 0, 1]


def esValido(x, y, n):
    return x >= 0 and x < n and y >= 0 and y < n


def solucionar(inicial, final, x, y, n):
    z = []
    pq.heapify(z)
    raiz = Node(inicial, None, 0, x, y, x, y)

    raiz.costo = calcularCosto(inicial, final, n)
    pq.heappush(z, raiz)
    while len(z) != 0:
        pq.heapify(z)
        print(z[0].matriz)
        min = pq.heappop(z)
        print(min.matriz, min.costo, 'papi')
        if min.costo == 0:
            # return solucion(min)
            # break
            return [[1, 2, 3], [1, 2, 3], [1, 2, -1]]

        for i in range(4):

            if esValido(min.x+fila[i], min.y+columna[i], n):

                hijo = Node([row[:] for row in min.matriz], min, min.nivel+1, min.x, min.y, min.x+fila[i], min.y+columna[i])

                hijo.costo = calcularCosto(hijo.matriz, final, n)
                print(hijo.matriz, hijo.costo, 'hijo')
                pq.heappush(z, hijo)

        return [[1, 2, 3], [1, 2, 3], [1, 2, -1]]


def solucion(raiz):

    if raiz is None:
        return
    solucion(raiz.padre)

    return raiz.matriz


def ayGonorrea():
    inicial = [[1,4,8], [-1,3,7],[5,2,6]]
    final =[[1,2,3],[4,5,6],[7,8,-1]]
    x = 1
    y = 0
    print(inicial[x][y])
    solucionar(inicial, final, x, y, 3)


# ayGonorrea()
