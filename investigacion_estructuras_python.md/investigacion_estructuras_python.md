


# Estructuras en python:

## Listas:
*Python conoce una serie de tipos de datos compuestos, utilizados para agrupar a otros Valores. La más versátil es la lista, que se puede escribir como una lista de Valores separados por comas (artículos) entre corchetes. Las listas pueden contener Elementos de diferentes tipos(numer), pero por lo general todos los elementos tienen el mismo tipo*
```py
vocales = ["a", "e", "i", "o", "u"]

```
**¿Por que las listas son mutables?**

*Una estructura mutable significa que se puede cambiar su contenido sin crear una nueva estructura, es decir que puedes cambiar un valor existente, agregar valores, eliminar valores* 

```py
numeros = [1, 2, 3]
numeros[0] = 99   # ← Cambias el 1 por 99
```

**¿Cuando resultan utiles?**

Las listas son útiles cuando necesitas guardar varios datos relacionados, por ejemplo:

Guardar calificaciones,guardar nombres de usuarios,almacenar valores que van cambiando,recorrer elementos con un bucle (for),añadir o quitar datos dinámicamente.

*Básicamente, cuando trabajas con múltiples valores que pueden cambiar.*

**Ejemplo de creacion, lectura, modificacion y eliminacion**
```py
numeros = [1,2,2,4,5,6]
print(numeros[0])

numeros[2] = 3

numeros.remove[2]
```
## Tuplas:
*Las tuplas son secuencias inmutables, típicamente utilizadas para almacenar colecciones de Datos heterogéneos (tales como las 2 tuplas producidas por el enumerate()Incorporado). Las tuplas también se utilizan para casos en los que una secuencia inmutable.*
```py
cedulas = (10023002, 1202021)
```
**¿Por que las listas son inmutables?**

*Decimos que algo es inmutable cuando no se puede modificar después de creado.
Esto significa que, con una tupla, NO puedes:*

Cambiar un elemento

Agregar elementos

Eliminar elementos

**¿Cuando resultan utiles?**

*Las tuplas son perfectas cuando necesitas datos que deben permanecer iguales durante toda la ejecución del programa. Realmente para eso es, investigue y este seria el resumen de muchas cosas.*

**Ejemplo de acceso y recorrido**

* **Acceso**

```py
cedulas = (100321120, 12030230)

print(cedulas[0])
print(cedulas[1])

```
* **Recorrido**

```py
for recorrer in cedulas:
    print(recorrer)

```

## Diccionario:

**¿Qué son y cómo almacenan la información?**

*Un dicionario es una estructura de datos que almacena informacion en forma de **clave** y **valor** ejemplo:*
* Clave: Identifica el dato(La clave en si no se puede repetir)
* Valor: Es el dato en si(Aveces puede cambiar)
```py
informacion = {"Cedula": 1232332, "Edad": 12}
```
*Los diccionarios funcionan internamente como una tabla hash.*

Esto significa:
* Cada clave se convierte en una especie de “código único”

* Python usa un algoritmo para convertir la clave en un número interno (hash).

Ese número sirve para encontrar el valor rápidamente

**Esta estructura permite que:**

* Consultar un valor por clave

* Agregar un nuevo par

* Modificar un valor

* Eliminar un elemento


*Las claves deben ser inmutables*

**Es decir, las claves pueden ser:**

* Cadenas **(str)**

* Números **(int, float)**

* Tuplas **(si su contenido no cambia)**
s
*Pero no pueden ser listas, porque las listas son mutables.*

**Diferencias clave frente a listas y tuplas:**
--PENDIENTE

**Ejemplos de agregar, consultar, modificar y eliminar elementos:**

**consultar:**
```py
dias = {"Lunes": 3, "Martes": 2, "Miercoles": 3, "Jueves": 4, "Viernes": 5}

print(dias["Lunes"])
```
**Agregar:**
```py
dias["Sabado"] = 6
dias["Domingo"]= 7
```
**Modificar:**
```py
dias["Lunes"] = 1
```
**Eliminar:**

```py
del dias["Domingo"]
```
## Match case:
**¿Qué es match–case y desde qué versión existe?**

*match–case es una estructura de control introducida en Python 3.10 (publicado en 2021).*
*Es una forma de hacer "pattern matching" o coincidencia de patrones, muy parecido a switch en otros lenguajes.*
*Sirve para comparar un valor contra múltiples casos y ejecutar la acción del caso que coincida.*
*Antes de Python 3.10, solo existían if, elif y else.*

**¿Para qué se usa?**

El match-case se usa para:

* Tomar decisiones según el valor de una variable

**Ejemplo:** *qué día es, qué número ingresó el usuario, qué comando escribió, etc.*

* Comparar un valor con varios patrones

**No solo números:** *también cadenas, booleans, rangos, tuplas, estructuras más complejas, etc.*

*Hacer código más limpio cuando hay muchas opciones.*

*Es mejor que escribir 10 elif seguidos.*

**Diferencias entre if, elif y else:**

| Característica                          | if / elif / else       | match-case                          |
| --------------------------------------- | ---------------------- | ----------------------------------- |
| Evalúa condiciones lógicas              | Sí                   | Sí                                |
| Ideal para varias opciones              | No (se vuelve largo) | Sí                                |
| Sintaxis más limpia                     |  No                   | Sí                                |
| Compara un valor con múltiples patrones | Pero es más difícil  | Muy fácil                         |
| Permite patrones complejos              | Limitado               | Sí (tuplas, estructuras, filtros) |
| Aparece desde                           | Python 1               | Python 3.
10                         |


**Situaciones donde usar match-case es más claro**

*match-case mejora la claridad cuando tienes muchas opciones definidas.*
*Ejemplos donde queda mejor:*

**Menu de opciones**
```py
match opcion:
    case 1: ...
    case 2: ...
    case 3: ...
```

**Clasificar valores:**
```py
match rol:
    case "admin":
    case "usuario":
    case "invitado":
```

**EJemplo sencillo:**
```py
opcion = int(input("Digita un número (1, 2 o 3): "))

match opcion:
    case 1:
        print("Elegiste la opción 1")
    case 2:
        print("Elegiste la opción 2")
    case 3:
        print("Elegiste la opción 3")
    case _:
        print("Opción inválida, intenta nuevamente.")

```