def analisis_de_cadena(cadena):
    balance = 0
    is_balanced = True
    i = 0

    # Se recorre cada caracter de la cadena
    while i < len(cadena):
        caracter = cadena[i]

        if caracter.isspace():
            i += 1
            continue

        # Si el caracter es un dígito, comenzamos a formar un número
        if caracter.isdigit():
            numero = caracter
            j = i + 1

            # Segundo ciclo para ver si los siguientes chars también son dígitos o un punto decimal
            while j < len(cadena):
                # Continuamos agregando dígitos al número
                if cadena[j].isdigit():
                    numero += cadena[j]
                    j += 1
                    continue

                # Si encontramos un punto seguido de un dígito, es un número flotante
                if cadena[j] == '.' and j + 1 < len(cadena) and cadena[j + 1].isdigit():
                    numero += cadena[j]
                    j += 1
                    while j < len(cadena) and cadena[j].isdigit(): 
                        numero += cadena[j]
                        j += 1
                    break
                break

            print(f"NUMERO {numero}", end=' ')
            i = j
            continue

        elif caracter.isalpha():
            operando = caracter
            j = i + 1
            while j < len(cadena) and cadena[j].isalpha():
                operando += cadena[j]
                j += 1
            print(f"OPERANDO {operando}", end=' ')
            i = j
            continue

        elif caracter == '(':
            balance += 1
            print("PAREN_IZQ (", end=' ')

        elif caracter == ')':
            if balance == 0:
                is_balanced = False
            else:
                balance -= 1
            print("PAREN_DER )", end=' ')
            
        elif caracter in "+-*/":
            print(f"OPERADOR {caracter}", end=' ')

        else:
            print(f"CARACTER_INVALIDO {caracter}", end=' ')

        i += 1

    if is_balanced and balance == 0:
        print("PARENTESIS BALANCEADOS")
    else:
        print("PARENTESIS NO BALANCEADOS")

    return cadena


if __name__ == "__main__":
    cadena = input("Ingrese la cadena: ")
    analisis_de_cadena(cadena)

