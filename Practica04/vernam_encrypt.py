'''
C =
1. Recibir M y sacar la longitud
2. Con la longitud calcular K
3. K son numeros aleatorios mod 26
4. Guardar Cm y k en un archivo
D =
5. Recibir archivos Cm y k
6. Obtener M en pantalla
7. Eliminar o borrar archivo k debido a un solo uso
'''
import random
import os

LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def parse_int_to_message(indices):
    encrypted_message = ""
    for num in indices:
        encrypted_message += LOWER_ALPHABET[num % 26]
    return encrypted_message

def parse_message_to_int(message):
    message_int = []
    for ch in message:
        for i in range(len(LOWER_ALPHABET)):
            if ch == LOWER_ALPHABET[i]:
                message_int.append(i)
    return message_int

def encrypt_message():
    message = str(input("\nWrite message to encrypt: "))
    message = message.replace(" ", "") # remove spaces
    message = message.lower()

    message_length = len(message) 

    message_int = parse_message_to_int(message=message)

    key_int = []
    # create a random key
    for _ in range(message_length):
        key_int.append(random.randint(0, 25))
    key_char = parse_int_to_message(indices=key_int)
    print(f"Random key is: {key_char}")

    # save key on a file
    with open("key.txt", "w") as f:
        f.write(key_char)
    print("Key saved at key.txt")

    encrypted_int = []
    for i in range(message_length):
        encrypted_int.append((message_int[i] + key_int[i]) % 26) # XOR between message and key

    encrypted_message = parse_int_to_message(indices=encrypted_int)

    return encrypted_message


def decrypt_message():
    message = str(input("\nWrite message to decrypt: "))
    message = message.replace(" ", "") # remove spaces
    message = message.lower()

    message_length = len(message) 

    message_int = parse_message_to_int(message=message)

    # read key and delete the file
    f = open("key.txt")
    key_char = f.read()
    print(f"Using the key: {key_char}")
    os.remove("key.txt")
    print("Key file deleted")

    key_int = parse_message_to_int(message=key_char)

    decrypted_int = []
    for i in range(message_length):
        decrypted_int.append((message_int[i] - key_int[i]) % 26) # XOR between message and key

    decrypted_message = parse_int_to_message(indices=decrypted_int)

    return decrypted_message

def main():
    option = 0
    while option != 3:
        print("""Welcome to Vernam Encrypt\n
[1]. Encrypt.
[2]. Decrypt. 
[3]. Close.\n""")
        option = int(input("Select an option: "))
        if option == 1:
            encrypted_message = encrypt_message()
            print(f"The encrypted message is: {encrypted_message}")
            print("\nPress any key to continue...")
            input('')
        if option == 2:
            decrypted_message = decrypt_message()
            print(f"The decrypted message is: {decrypted_message}")
            print("\nPress any key to continue...")
            input('')

if __name__ == "__main__":
    main()