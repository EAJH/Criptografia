def main():
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
                'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
                'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    alphabet2 = {v: k for k, v in alphabet.items()}
    upper_alphabet = set(alphabet2[i].upper() for i in alphabet2)

    a = True

    while a:
        print("\n-------- Cifrado Vigenère --------\n")
        menu()

        option = int(input("> "))
        final_message = ""

        if option == 1:
            text = input("Ingrese el mensaje que desea encriptar:\n")
            key = input("Ingrese la clave (solo letras):\n").lower()
            final_message = vigenere_encrypt(text, key, alphabet, alphabet2, upper_alphabet)
            print("Mensaje encriptado:", final_message)

        elif option == 2:
            text = input("Ingrese el mensaje que desea desencriptar:\n")
            key = input("Ingrese la clave (solo letras):\n").lower()
            final_message = vigenere_decrypt(text, key, alphabet, alphabet2, upper_alphabet)
            print("Mensaje desencriptado:", final_message)

        elif option == 3:
            a = False
            print("Hasta luego.")
        else:
            print("Ingrese una opción válida.")


def vigenere_encrypt(text, key, alphabet, alphabet2, upper_alphabet):
    result = ""
    key_index = 0
    key_len = len(key)

    for ch in text:
        if ch.lower() in alphabet:
            shift = alphabet[key[key_index % key_len]]
            idx = (alphabet[ch.lower()] + shift) % 26
            new_char = alphabet2[idx].upper() if ch in upper_alphabet else alphabet2[idx]
            result += new_char
            key_index += 1
        else:
            result += ch
    return result


def vigenere_decrypt(text, key, alphabet, alphabet2, upper_alphabet):
    result = ""
    key_index = 0
    key_len = len(key)

    for ch in text:
        if ch.lower() in alphabet:
            shift = alphabet[key[key_index % key_len]]
            idx = (alphabet[ch.lower()] - shift) % 26
            new_char = alphabet2[idx].upper() if ch in upper_alphabet else alphabet2[idx]
            result += new_char
            key_index += 1
        else:
            result += ch
    return result


def menu():
    print("1. Encriptar mensaje.")
    print("2. Desencriptar mensaje.")
    print("3. Salir.")


# Ejecución
main()
