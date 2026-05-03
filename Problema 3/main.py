def EsPar(Numero):
	if (Numero % 2 == 1):
		return False
	else:
		return True

def CalcularCollatz(Numero):
    Pasos = [Numero]
    while Numero > 1:
        if (EsPar(Numero) == False):
            Numero = Numero * 3 + 1
        else:
            Numero = Numero // 2
        Pasos.append(Numero)
    return Pasos

def solicitar_entero(Mensaje):
    while True:
        Valor = input(Mensaje).strip()
        try:
            Numero = int(Valor)
            if Numero > 0:
                return Numero
            print("Error: ingrese un número entero positivo válido.")
        except ValueError:
            print("Error: ingrese un número entero válido.")

def verificarCollatz():
    p = solicitar_entero('Ingrese el valor de p (inicio del intervalo): ')
    q = solicitar_entero('Ingrese el valor de q (fin del intervalo): ')

    # Validación de la regla q >= 100p
    if q < 100 * p:
        print(f"Error: q ({q}) debe ser al menos 100 veces p ({p})")
        return

    for i in range(p, q + 1):
        resultado = CalcularCollatz(i)
        print(f"n={i}: {' -> '.join(map(str, resultado))} \n")
    
    print("\nDemostrado...")   
    

if __name__ == "__main__":
    verificarCollatz()
    input("\nPresiona Enter para salir...")