from random import random

def vectorPorEscalar(vector, escalar):
    resultado = []
    for i in range(len(vector)):
        resultado.append(vector[i] * escalar)
    return resultado

def vectorMasEscalar(vector, escalar):
    resultado = []
    for i in range(len(vector)):
        resultado.append(vector[i] + escalar)
    return resultado

def vectorMenosVector(vector_a, vector_b):
    resultado = []
    for i in range(len(vector_a)):
        resultado.append(vector_a[i] - vector_b[i])
    return resultado

def vectorPorVector(vector_a, vector_b):
    resultado = []
    for i in range(len(vector_a)):
        resultado.append(vector_a[i] * vector_b[i])
    return resultado

def sumatoriaVectores(vector):
    resultado = 0
    for i in range(len(vector)):
        resultado += vector[i]
    return resultado

def procesoRegresion(x, y, w, b, alfa, tolerancia, iteraciones):
    for i in range(iteraciones):
        yh = vectorPorEscalar(x, w)
        yh = vectorMasEscalar(yh, b)

        error = vectorMenosVector(y, yh)
        sumatoria = sumatoriaVectores(error)
        loss = (1/len(error)) * (sumatoria**2)
    
        if(loss <= tolerancia):
            print()
            print("-=[ Ecuación Resultante ]=-")
            print("{}x + {}".format(w, b))
            print()
            print("Se utilizaron {} iteraciones.".format(i+1))

            r = abs(1 - loss)
            return r
        
        dw = vectorPorVector(error, x)
        dw = sumatoriaVectores(dw)
        dw *= (-2/len(error))

        db = sumatoriaVectores(error)
        db *= (-2/len(error))

        w -= alfa * dw
        b -= alfa * db

if __name__ == "__main__":
    w = 0
    b = 0
    x = [-0.425602809, 1.534850182, 0.846241656, -0.036614543, 0.291758403, -0.651090081, 0.471038009, -1.252575438 ,1.147956484, -1.023822386]
    y = [-38.23241509, 142.4837453, 79.00724804, -2.375158556, 27.89452823, -59.01801626, 44.42066896, -114.4634285, 106.8195677, -93.37678504]

    print(procesoRegresion(x, y, w, b, 0.55, 1e-3, 1000))