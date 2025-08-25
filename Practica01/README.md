# Práctica 1. Cifrado de César

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

En esta práctica se implementó el **algoritmo de Cifrado de César**, un método clásico de criptografía por sustitución. El programa permite **encriptar y desencriptar mensajes** mediante un número de corrimientos en el alfabeto, considerando tanto letras minúsculas como mayúsculas y manteniendo los espacios.

## Qué y cómo se logró

- Se definieron diccionarios para mapear letras a índices numéricos y viceversa, incluyendo la letra **ñ**.  
- Se desarrollaron dos funciones principales:  
  - `encrypt(n, k)` → aplica el corrimiento positivo (cifrado).  
  - `decrypt(n, k)` → aplica el corrimiento inverso (descifrado).  
- Se diseñó un menú interactivo que permite al usuario elegir entre **encriptar, desencriptar o salir**.  
- Se garantizó que el mensaje final conserve el formato original (mayúsculas y espacios).

De esta forma, se logró un programa funcional que demuestra de manera práctica cómo opera este cifrado histórico.

---
