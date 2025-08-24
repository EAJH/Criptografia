'''
k e y a b
c d f g h
i l m n o
p q r s t
u v w x z
'''

# In this algorithm i and j are the same

def search_coordinates(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return [i, j]
            
def remove_duplicates_key(key):
    ch_key = []
    for i in range(len(key)):
        if key[i] not in ch_key:
            ch_key.append(key[i])
    return ch_key

def create_matrix(key):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_key = remove_duplicates_key(key)
    for ch in new_key:
        if ch in alphabet:
            alphabet.remove(ch)
    alphabet = new_key + alphabet
    matrix = [alphabet[i:i + 5] for i in range(0, len(alphabet), 5)] # create lists of 5 elements and append into matrix
    return matrix

def encrypt_message():
    message = str(input("\nWrite message to encrypt: "))
    message = message.replace(" ", "") # remove spaces
    message = message.lower()

    message_length = len(message) # message divisible in syllables
    if message_length % 2 != 0:
        if message[message_length - 1] != "x" and message[message_length - 1] != "q":
            message += "x"
        elif message[message_length - 1] == "x":
            message += "q"
        elif message[message_length - 1] == "q":
            message += "x"

    key = str(input("Key str value: "))
    
    matrix = create_matrix(key=key)

    encrypted_message = ""
    for i in range(2, message_length + 2, 2):
        syllable = message[i - 2:i]
        coords_1 = search_coordinates(matrix=matrix, ch=syllable[0])
        coords_2 = search_coordinates(matrix=matrix, ch=syllable[1])
        if coords_1[0] == coords_2[0]: # same row move to the right
            if coords_1[1] + 1 == 5: # made circular
                encrypted_message += matrix[coords_1[0]][0]
            else:
                encrypted_message += matrix[coords_1[0]][coords_1[1] + 1]
            if coords_2[1] + 1 == 5:
                encrypted_message += matrix[coords_2[0]][0]
            else:
                encrypted_message += matrix[coords_2[0]][coords_2[1] + 1]
        elif coords_1[1] == coords_2[1]: # same column move down
            if coords_1[0] + 1 == 5: # made circular
                encrypted_message += matrix[0][coords_1[1]]
            else:
                encrypted_message += matrix[coords_1[0] + 1][coords_1[1]]
            if coords_2[0] + 1 == 5:
                encrypted_message += matrix[0][coords_2[1]]
            else:
                encrypted_message += matrix[coords_2[0] + 1][coords_2[1]]
        elif coords_1[0] != coords_2[0] and coords_1[1] != coords_2[1]: # different positions create a square or rectangle and take the contrary corners
            encrypted_message += matrix[coords_2[0]][coords_1[1]]
            encrypted_message += matrix[coords_1[0]][coords_2[1]]
    return encrypted_message

def decrypt_message():
    message = str(input("\nWrite message to decrypt: "))
    message = message.replace(" ", "") # remove spaces
    message = message.lower()

    message_length = len(message) # message divisible in syllables

    key = str(input("Key str value: "))
    
    matrix = create_matrix(key=key)

    encrypted_message = ""
    for i in range(2, message_length + 2, 2):
        syllable = message[i - 2:i]
        coords_1 = search_coordinates(matrix=matrix, ch=syllable[0])
        coords_2 = search_coordinates(matrix=matrix, ch=syllable[1])
        if coords_1[0] == coords_2[0]: # same row move to the right
            if coords_1[1] - 1 == -1: # made circular
                encrypted_message += matrix[coords_1[0]][4]
            else:
                encrypted_message += matrix[coords_1[0]][coords_1[1] - 1]
            if coords_2[1] - 1 == -1:
                encrypted_message += matrix[coords_2[0]][4]
            else:
                encrypted_message += matrix[coords_2[0]][coords_2[1] - 1]
        elif coords_1[1] == coords_2[1]: # same column move down
            if coords_1[0] - 1 == -1: # made circular
                encrypted_message += matrix[4][coords_1[1]]
            else:
                encrypted_message += matrix[coords_1[0] - 1][coords_1[1]]
            if coords_2[0] - 1 == -1:
                encrypted_message += matrix[4][coords_2[1]]
            else:
                encrypted_message += matrix[coords_2[0] - 1][coords_2[1]]
        elif coords_1[0] != coords_2[0] and coords_1[1] != coords_2[1]: # different positions create a square or rectangle and take the contrary corners
            encrypted_message += matrix[coords_2[0]][coords_1[1]]
            encrypted_message += matrix[coords_1[0]][coords_2[1]]
    return encrypted_message

def main():
    option = 0
    while option != 3:
        print("""Welcome to Wheatstone-Playfair Encrypt\n
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