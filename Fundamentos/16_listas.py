# listas

numbers = [1, 2, 3]
print (numbers)
print (type(numbers))

tasks = ['make a dishes', 'play videogames']
print (tasks)


#las listas pueden tener diferentes elementos
types = [1, True, 'hola']
print (types )

#Acá puedo navegar por los elementos de la lista

print (numbers[0])
print (tasks [0])

#puedo almacenar información de diferentes tipos en una estructura de datos

text = 'Hola'
# text [0] = 'W' Esto nos da un error por que las cadenas de texto no se pueden editar

tasks [0] = "watch platzi courses"
print (tasks)
tasks [0] = 'do the dishes' # podemos hacer todos los cambios que queramos

#podemos recorrer todos los elementos de una lista
print (numbers [:3])

#podemos interrogar a nuestra lista, hay un True dentro de la lista types
print (True in types)
print ('hola' in True)





