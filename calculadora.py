def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def division (a, b):
    if b == 0:
        raise ValueError("No se puede dividir por 0")
    return a / b