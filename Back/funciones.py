import numpy as np
def fibonacci(n):
    n = n**2
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
    return answer

def primos(n):
    arrayLength = 1
    maxToCheck = 1
    if n == 3:
        arrayLength = 25
        maxToCheck = 5
    elif n == 4:
        arrayLength = 55
        maxToCheck = 8
    else:
        arrayLength = 100
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
    return answer



def pares(n):
    n = n**2
    answer = []
    add = 2
    answer.append(add)
    while n != 1:
        add += 2
        answer.append(add)
        n -= 1
    return answer

def impares(n):
    n = n**2
    answer = []
    add = 1
    answer.append(add)
    while n != 1:
        add += 2
        answer.append(add)
        n -= 1
    return answer

def potenciasDeDos(n):
    n = n**2
    answer = []
    i = n
    while n - i != n:
        add = 2**(n-i)
        answer.append(add)
        i -= 1
    return answer

def cuadratica(n):
    n = n**2
    answer = []
    i = 1
    while i != n+1:
        answer.append(i**2)
        i += 1
    return answer

print(fibonacci(3))
print(cuadratica(3))
print(pares(3))
print(impares(3))
print(primos(3))