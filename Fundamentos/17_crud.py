"""

Métodos de las listas

clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.





"""

#CRUD Create, Read, Update & Delete

#Create
numbers = [1, 2, 3, 4, 5]
#Read
print (numbers [1])
# Update
numbers [-1] = 10
print (numbers)
# append(): Añade un ítem al final de la lista.
numbers.append (700)
print (numbers)
print(('*')*20)
#insert(): Agrega un ítem a la lista en un índice específico, cuándo se agrega, todo el indice se corre hacia la derecha
numbers.insert (0, 'hola')
print (numbers)
numbers.insert (3, 'change')
print (numbers)

#fusionar listas
tasks = ['todo 1','todo 2','todo 3']
new_list = numbers + tasks
print (new_list)

#si quiero actualizar un valor específico, primero tengo que saber dónde está
#con el método index puedo saber en qué posición está un elemento para reemplazarlo

index = new_list.index('todo 2')
new_list[index]= 'todo changed '
print (new_list)

#Delete
#remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.

new_list.remove('todo 1')
print (new_list)

#pop(): Extrae un ítem de la lista y lo borra. Podemos dejarlo sin parámetro, o darle uno. 
new_list.pop()
print (new_list)

new_list.pop(0)
print(new_list)

#reverse(): Le da la vuelta a la lista actual.
new_list.reverse()
print(new_list)

numbers_a = [1, 4 , 6 ,3]
numbers_a.sort()
print (numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print (strings)

#pero sort no puede mezclar datos mezclados como por ejemplo en la lista new_list pues tiene strings numbers y bool
# new_list.sort()

