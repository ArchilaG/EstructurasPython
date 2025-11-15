"""
    Diccionarios — Inventario básico

Crear un diccionario con al menos cuatro productos y sus precios. El usuario elige una acción:

    Agregar un nuevo producto con su precio.
    Consultar el precio de un producto existente.
    Modificar el precio de un producto existente.
    Eliminar un producto del inventario.

Al terminar la acción seleccionada, mostrar cuántos productos hay actualmente y el promedio de precios.


"""

tienda = {"Papa": 1000, "Huevo": 500, "Banano": 600, "Yuca": 4000}

print(tienda["Huevo"])
tienda["Papa"] = 800
print(tienda["Papa"]) #La papa bajo

del tienda["Banano"]
print(tienda)

print("=====================================================")
print(f"Hay {tienda} actualmente")


print("=================================================")
print("Promedio de precios es de: ")
    
suma = sum(tienda.values())
promedio = round(suma/len(tienda), 1)
print(promedio)