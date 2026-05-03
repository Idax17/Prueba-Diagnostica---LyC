#3) Escriba un código que verifique si se cumple la conjetura 
#de collatz en enteros de un intervalo [p,q]. La conjetura indica 
#que para cualquier número entero positivo n se aplica:

#Si n es par → n = n / 2, Si n es impar → n = 3n + 1,

#Ejemplo n=6: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#        n=7: 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20...
#        n=8: 8 → 4 → 2 → 1
#Demostrado...

#Regla q ≥ 100p para poder aplicar la demostración.

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

def solicitar_entero(Valor):
    while True:
        try:
            Numero = int(Valor)
            if Numero > 0:
                return Numero
            print("Error: ingrese un número entero positivo válido.")
            
        except ValueError:
            print("Error: ingrese un número entero válido.")

def verificarCollatz():
    p = solicitar_entero(input('Ingrese el valor de p (inicio del intervalo): ').strip())
    q = solicitar_entero(input('Ingrese el valor de q (fin del intervalo): ').strip())

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