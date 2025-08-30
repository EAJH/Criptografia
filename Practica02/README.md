# Práctica 2. Cifrado de Vigenère y Método Kasiski

**Integrantes:**
- López Reyes Alam  
- García Martínez Luis Eduardo  
- Juárez Herrera Erick Adrián  
- Hernández García Pilar Jaqueline
- Romero Domínguez Ricardo Damián
- Benitez Pérez Michelle Paulina  

**Fecha:** 19-08-25  

---

## Descripción breve

En esta práctica se implementó el **algoritmo de Cifrado de Vigenère y método Kasiski**, un método clásico de criptografía. El programa permite **encriptar y desencriptar mensajes** mediante un número de corrimientos en el alfabeto, así como una cantidad de alfabetos equivalente a la cantidad de letras que este tenga, considerando tanto letras minúsculas como mayúsculas y manteniendo los espacios. Adicionalmente, se implementa el método Kasiski mostrando el proceso por el cual se rige este método, como encontrar sub patrones dentro del mensaje, calcular las distancias entre bloques repetidos, obtener el MCD, así como la separación del mensaje y obtención de la llave.

## Qué y cómo se logró

- Se definieron diccionarios para mapear letras a índices numéricos y viceversa.  
- Se desarrollaron dos funciones principales:  
  - `vigenere_encrypt(text, key, alphabet, alphabet2, upper_alphabet)` → aplica el algoritmo de cifrado
  Vigenère.  
  - `vigenere_decrypt(text, key, alphabet, alphabet2, upper_alphabet)` → aplica el algoritmo de descifrado
  Vigenère.  
- Se diseñó un menú interactivo que permite al usuario elegir entre **encriptar, desencriptar o salir**.  
- Se garantizó que el mensaje final conserve el formato original (mayúsculas y espacios).

De esta forma, se logró un programa funcional que demuestra de manera práctica cómo opera este algoritmo de cifrado.

- Adicionalmente, se programó la metodología Kasiski, el cual opera tras el llamado de funciones con base 
en el siguiente orden:

1. `patrones()`→ Para encontrar patrones que se repiten.
2. `longitudClave()`→ Para calcular la posible longitud de la llave.
3. `separacionMensaje()`→ Para separar el texto cifrado en bloques.
4. `obtencionLlave()`→ Para ejecutar el proceso de análisis de frecuencias y encontrar la llave.

Finalmente, el código imprime en terminal los resultados de cada paso: los patrones encontrados, los bloques
del mensaje separado, así como la llave deducida.

---
