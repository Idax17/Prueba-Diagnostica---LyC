#2) Dado una cadena C, valide si C se encuentra en notación FEN 
#(Forsyth-Edwards Notation), Forsyth–Edwards Notation. FEN 
#(Wikipedia, 2025).

#Ejemplo: 4t1r1/p1p2pp1/1d1p3p/1P3P2/1P6/2c1D3/PA4PP/4T1R1/

def analisis_de_cadena(cadena):
    i = 0  
    previo = ''  # Almacena el caracter anterior para verificar '/' consecutivos

    contador_slash = 0  # Contador de '/' para asegurar que haya exactamente 8

    casillas_en_seccion = 0 # Contador de casillas en la sección actual

    # Contadores para cada letra y sus límites
    contador_letras = {'r': 0, 'R': 0, 'd': 0, 'D': 0, 'p': 0, 'P': 0, 'a': 0, 'A': 0, 'c': 0, 'C': 0, 't': 0, 'T': 0}
    limites_letras = {'r': 1, 'R': 1, 'd': 1, 'D': 1, 'p': 8, 'P': 8, 'a': 2, 'A': 2, 'c': 2, 'C': 2, 't': 2, 'T': 2}

    if len(cadena) == 0 or cadena[0] == '/':
        return "La cadena está vacía o comienza con '/'"

    # Se recorre cada caracter de la cadena
    while i < len(cadena):
        caracter = cadena[i]

        if caracter == '/' and previo == '/':
            return "Dos '/' consecutivos"

        if caracter.isspace():
            return "Contiene espacios"

        # Si el caracter es un dígito, indica casillas vacías
        if caracter.isdigit():
            if caracter < '1' or caracter > '8':
                return "Dígito no válido (debe ser entre 1 y 8)"
            
            casillas_en_seccion += int(caracter)

            if casillas_en_seccion > 8:
                return "Sección excede 8 casillas"

        elif caracter.isalpha():
            if caracter in "rtpdcaRTPDCA":

                if caracter in contador_letras:
                    contador_letras[caracter] += 1

                    if contador_letras[caracter] > limites_letras[caracter]:
                        return f"Más de {limites_letras[caracter]} '{caracter}'"
                    
                casillas_en_seccion += 1

                if casillas_en_seccion > 8:
                    return "Sección excede 8 casillas"
                print(f"{caracter}", end=' ')

            else:
                return "Letra no válida (debe ser una pieza de ajedrez)"
            i += 1
            previo = caracter
            continue

        elif caracter == '/':
            if casillas_en_seccion != 8:
                return "Sección no tiene 8 casillas"
            
            contador_slash += 1

            if contador_slash > 8:
                return "No puede haber más de 8 '/'"
            
            casillas_en_seccion = 0

            i += 1
            previo = caracter
            continue

        else:
            return "Carácter no válido"

        previo = caracter
        i += 1

    if cadena[-1] != '/':
        return "Debe terminar con '/'"

    if contador_slash != 8:
        return "No tiene exactamente 8 '/'"

    return True


if __name__ == "__main__":
    cadena = input("Ingrese la cadena: ")
    result = analisis_de_cadena(cadena)
    if result == True:
        print("CADENA VALIDA")
    else:
        print(f"CADENA INVALIDA: {result}")

