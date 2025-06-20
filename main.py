from matematicas import add, mul, rest
if __name__ == '__main__':
    print("Main program")
    accion = input("Que quieres hacer? 's' para sumar, 'm' para multiplicar y 'r' para restar:  ")

    x = int(input("Ingresa primer numero: "))
    y = int(input("Ingresa segundo numero: "))

    if accion == 's':
        result = add(x, y)
        print(f"Resultado: {result}")
    elif accion == 'm':
        result = mul(x, y)
        print(f"Resultado: {result}")
    elif accion == 'r':
        result = rest(x, y)
        print(f"Resultado: {result}")
    else:
        print("Accion no reconocida")
