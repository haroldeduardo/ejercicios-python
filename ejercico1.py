def devolver_distintos(num1,num2,num3):
    
    numeros = sorted([int(num1), int(num2), int(num3)])
    suma = sum(numeros)

    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    else:
        return numeros[1]

print(devolver_distintos(1,8,4))


