
#Solución de un sistema de ecuaciones

# Las variables a utilizar seran declaradas como marices
matriz =[]
resultado =[]


# Seccion de funciones a utilizar
def matv(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz


# Captura de datos muestra matriz

def datos (n):
    matriz = matv(n)
    for x in range(n):
        for y in range(n):
            matriz[x][y] = float(input('Valor de [ '+ str(x ) +'][ ' +str(y ) +']'))
        resultado.append(float(input('valor del resultado de la ecuacion')))


# Uso del metodo de Gaus
def gauss(n):
    for z in range(n - 1):
        for x in range(1,n-z):
            if (matriz[z][z] != 0):
                p = matriz[x + z][z] / matriz[z][z]
                for y in range(n):
                    matriz[x + z][y] = matriz[x + z][y] - (matriz[z][y] * p)
                resultado[x + z] = resultado[x + z] - (resultado[z] * p)


# Uso del metodo de Gauss Jordan
def gjor(n):
    for z in range(n - 1, 0, -1):
        for x in range(z):
            if (matriz[z][z] != 0):
                p = matriz[x][z] / matriz[z][z]
                matriz[x][z] = matriz[x][z] - (matriz[z][z] * p)
                resultado[x] = resultado[x] - (resultado[z] * p)


# Calculo de las soluciones (si es que existen)
def solucion(n):
    print("\n")
    for i in range(n):
        if (matriz[i][i] != 0): matrizsolucion = True
        else:
            matrizsolucion = False
            break
    if (matrizsolucion == True):
        for i in range(n):
            if (i == 0): print(f"el valor de la variable x es {resultado[i] / matriz[i][i]}")
            if (i == 1): print(f"El valor de la variable y es {resultado[i] / matriz[i][i]}")
            if (1 == 2): print(f"El valor de la variable z es {resultado[i] / matriz[i][i]}")

    else:
        print('Matriz sin solución')


# Llamado de las diferentes funciones


n = int(input('Tamaño de la matriz : '))

datos(n)
gauss(n)
gjor(n)
solucion(n)

