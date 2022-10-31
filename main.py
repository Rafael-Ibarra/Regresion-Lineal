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
    n = len(x)
    for i in range(iteraciones):
        yh = vectorPorEscalar(x, w)
        yh = vectorMasEscalar(yh, b)

        error = vectorMenosVector(y, yh)
        sumatoria = sumatoriaVectores(error)
        loss = (1/n) * (sumatoria**2)
    
        if(loss <= tolerancia):
            r = abs(1 - loss)
            return yh, r, w, b
        
        dw = vectorPorVector(error, x)
        dw = sumatoriaVectores(dw)
        dw *= (-2/n)

        db = sumatoriaVectores(error)
        db *= (-2/n)

        w -= alfa * dw
        b -= alfa * db

if __name__ == "__main__":
    w = random()
    b = random()
    x = [0.229603789, -1.069684487, 0.724914348, 0.037690034, -0.322328644, 0.233248992, -0.471233456, 1.68446954, 0.201323551, -0.579319582]
    y = [16.90056009, -78.68020895, 53.33755804, 2.782627519, -23.70176609, 17.16871565, -34.65579128, 123.9262218, 14.82015431, -42.6070329]

    print(procesoRegresion(x, y, w, b, 0.62, 1e-3, 1000))