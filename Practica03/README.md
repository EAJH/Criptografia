# Práctica 3. Cifrado Wheatstone - Playfair

**Integrantes:**
- López Reyes Alam  
- García Martínez Luis Eduardo  
- Juárez Herrera Erick Adrián  
- Hernández García Pilar Jaqueline
- Romero Domínguez Ricardo Damián
- Benitez Pérez Michelle Paulina  

**Fecha:** 21-08-25  

---

## Descripción breve

En esta práctica se implementó el **algoritmo de Cifrado Wheatstone - Playfair**, un método moderno de criptografía. El programa permite **encriptar y desencriptar mensajes** aplicando las reglas vistas en clase para el algoritmo playfair, estas reglas son:

1. Mismo renglón → La letra se transforma en su consecuente a la derecha.
2. Distinto renglón y columna → Generar un cuadro entre las letras correspondientes e intercambiarlas por las de la esquina.
3. Misma columna → La letra se transforma en su consecuente hacia abajo.

Es importante recalcar esto, pues en este algoritmo, las reglas se definen antes de aplicar el algoritmo y pueden cambiar entre los usuarios del mismo.

## Qué y cómo se logró

- Se creó un menú principal dentro del cual se llaman a las dos funciones principales del programa:  
  - `encrypt_message()` → aplica el algoritmo de cifrado de playfair con base a las reglas establecidas.  
    - Dentro del proceso de cifrado se siguen los siguientes pasos:
      1. Eliminación de espacios y ajuste de longitud del mensaje para uso de bloques.
      2. Construcción de la matriz `5x5`con base a la llave ingresada y el alfabéto inglés.
      3. Para cada par de letras correspondientes a cada bloque establecido en el mensaje, se localiza su 
         posición dentro de la matriz de `5x5`creada anteriormente y se aplican las reglas establecidas
         inicialmente.
      4. Se muestra en pantalla el mensaje cifrado.
  - `decrypt_message()` → aplica el algoritmo de descifrado de playfair con base a las reglas establecidas.  
    - Dentro del proceso de descifrado se siguen los siguientes pasos:
      1. Se aplica la lógica inversa a lo descrito dentro del proceso de cifrado.
      2. Se muestra en pantalla el mensaje descifrado.
- Se diseñó un menú interactivo que permite al usuario elegir entre **encriptar, desencriptar o salir**.  



---
