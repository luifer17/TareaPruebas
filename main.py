def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No se puede dividir entre cero")

# Ejemplo de uso
resultado_suma = suma(5, 3)
print(f"Suma: {resultado_suma}")
