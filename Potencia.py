def potencia(base, exponente):
    resultado = 1
    for _ in range(int(exponente)):
        resultado *= base
    return resultado
