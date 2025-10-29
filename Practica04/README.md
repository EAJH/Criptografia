# Práctica 4. Cifrado Vernam

**Integrantes:**
- López Reyes Alam  
- García Martínez Luis Eduardo  
- Juárez Herrera Erick Adrián  
- Hernández García Pilar Jaqueline
- Romero Domínguez Ricardo Damián
- Benitez Pérez Michelle Paulina 

Este proyecto es una implementación simple en Python del **Cifrado de Vernam** (también conocido como *One-Time Pad* o Cifrado de un solo uso). El script permite cifrar y descifrar mensajes utilizando una clave aleatoria que se genera durante el proceso de cifrado y se autodestruye después del descifrado.

## 1. Descripción Breve de la Implementación

La implementación utiliza aritmética modular para cifrar y descifrar mensajes. El algoritmo se limita al alfabeto inglés de 26 letras minúsculas.

* **Cifrado:** Se genera una clave aleatoria ($K$) de la misma longitud que el mensaje ($M$). El criptograma ($C$) se obtiene sumando el valor numérico de cada caracter del mensaje con el valor numérico del caracter correspondiente en la clave, aplicando la operación módulo 26.
    * $C_i = (M_i + K_i) \pmod{26}$
* **Descifrado:** Se utiliza la misma clave ($K$) leída desde el archivo. El mensaje original ($M$) se recupera restando el valor de la clave al valor del criptograma, aplicando también módulo 26.
    * $M_i = (C_i - K_i) \pmod{26}$

Una característica clave de esta implementación es que la clave se almacena en un archivo (`key.txt`) durante el cifrado y **se elimina automáticamente** (`os.remove("key.txt")`) después de ser usada una vez para descifrar, respetando el principio de "un solo uso" del cifrado de Vernam.

## 2. Qué se hizo y cómo se hizo

El script está estructurado en torno a un menú principal (`main`) que permite al usuario elegir entre cifrar, descifrar o salir. Utiliza funciones auxiliares para convertir texto a números y viceversa, y funciones principales para manejar la lógica de cifrado y descifrado.

### Descripción de Funciones

Aquí se detallan las funciones utilizadas y su propósito:

* **`parse_int_to_message(indices)`**
    * **Parámetros:** `indices` (lista de enteros).
    * **Resultado:** Una cadena de caracteres (string).
    * **Descripción:** Convierte una lista de índices numéricos (0-25) a su correspondiente cadena de texto en el alfabeto (ej. `[0, 1, 2]` -> `"abc"`).

* **`parse_message_to_int(message)`**
    * **Parámetros:** `message` (string).
    * **Resultado:** Una lista de enteros.
    * **Descripción:** Convierte una cadena de texto a su correspondiente lista de índices numéricos (ej. `"abc"` -> `[0, 1, 2]`).

* **`encrypt_message()`**
    * **Parámetros:** Ninguno. Pide el mensaje por consola.
    * **Resultado:** El mensaje cifrado (string).
    * **Descripción:**
        1.  Pide al usuario el mensaje a cifrar.
        2.  Limpia el mensaje (quita espacios y convierte a minúsculas).
        3.  Calcula la longitud del mensaje.
        4.  Genera una clave aleatoria (`key_int`) de la misma longitud (usando `random.randint(0, 25)`).
        5.  Guarda la versión en texto de la clave en el archivo `key.txt`.
        6.  Realiza la operación $(M_i + K_i) \pmod{26}$ para cada caracter.
        7.  Devuelve el criptograma resultante.

* **`decrypt_message()`**
    * **Parámetros:** Ninguno. Pide el criptograma por consola.
    * **Resultado:** El mensaje descifrado (string).
    * **Descripción:**
        1.  Pide al usuario el mensaje a descifrar.
        2.  Limpia el criptograma (quita espacios y convierte a minúsculas).
        3.  Lee la clave (string) desde el archivo `key.txt`.
        4.  **Elimina el archivo `key.txt`** usando `os.remove()`.
        5.  Convierte la clave de string a una lista de enteros (`key_int`).
        6.  Realiza la operación $(C_i - K_i) \pmod{26}$ para cada caracter.
        7.  Devuelve el mensaje original.

* **`main()`**
    * **Parámetros:** Ninguno.
    * **Resultado:** Ninguno.
    * **Descripción:** Es la función principal que ejecuta el programa. Muestra un menú de bienvenida y gestiona un bucle `while` que permite al usuario seleccionar una opción (1: Cifrar, 2: Descifrar, 3: Salir) y llama a la función correspondiente.

### Flujo General del Programa

1.  El script se ejecuta y entra en la función `main()`.
2.  Se muestra el menú de opciones.
3.  El usuario introduce un número (1, 2 o 3).
4.  **Si es 1 (Cifrar):**
    * Se llama a `encrypt_message()`.
    * El usuario introduce el mensaje.
    * Se genera la clave, se guarda en `key.txt` y se calcula el criptograma.
    * Se imprime el criptograma y la clave generada.
5.  **Si es 2 (Descifrar):**
    * Se llama a `decrypt_message()`.
    * El usuario introduce el criptograma.
    * Se lee la clave de `key.txt`.
    * Se elimina `key.txt`.
    * Se calcula el mensaje original.
    * Se imprime el mensaje original y la clave que se utilizó.
6.  **Si es 3 (Salir):**
    * La condición del bucle `while` se vuelve falsa y el programa termina.
7.  El bucle se repite hasta que el usuario elija la opción 3.