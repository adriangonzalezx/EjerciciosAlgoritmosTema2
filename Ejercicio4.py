def modificar(lista):
    # Copiar la lista original para no modificarla
    nueva_lista = lista[:]
    
    # Borrar los elementos duplicados
    nueva_lista = list(set(nueva_lista))
    
    # Ordenar la lista de mayor a menor
    nueva_lista.sort(reverse=True)
    
    # Eliminar todos los números impares
    nueva_lista = [num for num in nueva_lista if num % 2 == 0]
    
    # Realizar la suma de todos los números que quedan
    suma_total = sum(nueva_lista)
    
    # Añadir la suma como primer elemento de la lista
    nueva_lista.insert(0, suma_total)
    
    return nueva_lista

# Ejemplo de uso
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nueva_lista = modificar(lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))  # Comprobación de que la suma concuerda

