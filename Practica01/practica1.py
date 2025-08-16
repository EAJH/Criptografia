# k es el índice de la letra en cuestion conforme al abecedario

def main():

    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22 , 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    alphabet2 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'ñ', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    upper_alphabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    a = True
    
    
    while (a):
        print("\n-------- Práctica 1. Cifrado César --------\n")
        menu()

        option = int(input())
        encryption = []
        decryption = []
        final_message = ""

        if(option == 1):
            messageEncrypted = input("Ingrese el mensaje que se desea encriptar: \n")
            messageEncrypted_lower = messageEncrypted.lower()
            print("Ingrese la cantidad de corrimientos (n): ")
            n = int(input())

            for caracter  in messageEncrypted_lower:
                if caracter == ' ':
                    encryption.append(caracter)
                else:
                    k = alphabet[caracter]
                    caracter_encriptado = encrypt(n,k)
                    encryption.append(caracter_encriptado)

            j = 0
            for i in encryption:
                
                if i == ' ':
                    final_message += ' '
                elif messageEncrypted[j] in upper_alphabet:
                    final_message += (alphabet2[i].upper())
                else:
                    final_message +=(alphabet2[i])
                j += 1


            print("El mensaje encriptado es: ", final_message)

        elif(option == 2):
            messageDecrypted = input("Ingrese el mensaje que se desea desencriptar: \n")
            messageDecrypted_lower = messageDecrypted.lower()
            print("Ingrese la cantidad de corrimientos (n): ")
            n = int(input())

            for caracter  in messageDecrypted_lower:
                if caracter == ' ':
                    decryption.append(caracter)
                else:
                    k = alphabet[caracter]
                    caracter_encriptado = decrypt(n,k)
                    decryption.append(caracter_encriptado)

            j = 0
            for i in decryption:
                if i == ' ':
                    final_message += ' '
                elif messageDecrypted[j] in upper_alphabet:
                    final_message += (alphabet2[i].upper())
                else:
                    final_message+=(alphabet2[i])
                j += 1

            print("El mensaje desencriptado es: ", final_message)


        elif(option == 3):
            a = False
            print("\nHasta luego.")


        else:
            print("Ingrese una opción válida.")


def encrypt(n, k):
    a = ((k+n)) % 27
    return a


def decrypt(n, k):
    a = (k-n) % 27
    return a


def menu():
    print("Ingrese la opción deseada: \n\n")
    print("1. Encriptar mensaje.\n")
    print("2. Desencriptar mensaje. \n")
    print("3. Salir.\n")


# Ejecución del programa
main()