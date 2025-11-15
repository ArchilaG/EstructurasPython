"""

Tuplas — Catálogo estático

Crear una tupla con seis valores numéricos distintos. Debido a que no se puede modificar directamente, se debe mostrar el resultado de cada operación sin alterar la tupla original:

    Cómo quedaría si se agregara un nuevo valor al final.
    Cómo quedaría si un valor se reemplazara por otro.
    Cómo quedaría si se eliminara un valor por su posición.
    Mostrar todos los valores con sus posiciones.

Además, se debe determinar manualmente:

    El valor mayor.
    El valor menor.
    La suma total.
    La posición del mayor.



"""
numeros = (1,2,3,4,5,6)

numeroLista = list(numeros)
print(numeros)
print("==============")
print("Se añade un nuevo valor y es: ")

numeroLista.append(7)
print(numeroLista)

numeroLista[0] = 10
print("==============")
print("Se cambio un nuevo valor y es: ")
print(numeroLista)

del numeroLista[0]
print("==============")
print("Se quita un  valor y es: ")
print(numeroLista)

numeroTupla = tuple(numeroLista)
print("==============")
print("Total de numeros que hay y es de: ")
print(len(numeroTupla))

print("==============")
print("Mostrar todos los valores con sus posiciones: ")
for i in range(len(numeros)):
    print(i, numeros[i])

print("==============")
print("Valor mayor: ")
print(max(numeros))

print("==============")
print("Valor menor: ")
print(min(numeros))

print("==============")
print("Suma total: ")
print(sum(numeros))

print("==============")
print("Posicion del mayor: ")
print(numeros.index(max(numeros)))
