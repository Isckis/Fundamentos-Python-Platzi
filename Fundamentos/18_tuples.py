#Las tuplas son un tipo de conjunto de datos que se parecen a las listas, pero que no se pueden editar

numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print (numbers)
print (type (numbers))
#podemos interrogar a nuestra tupla por la posición de elementos, el primero, el último. 
print ('0=>', numbers [0])
print ('-1=>', numbers [-1])


print (strings)
print (type (strings))

#Las tuplas al no poder ser modificadas no cuentan con mecanismos como .append () y nos va a tirar error
#numbers.append(10)
#print(numbers)
#numbers[1] = 'change'

#Podemos interrogar a la tupla por la ubicación de sus elementos como .index()
print (strings)
print(strings.index('zule'))

#Podemos contar sus elementos con .count()
print(strings.count('nico'))

#no podemos hacer cambios en la tupla pero la podemos transformar a una lista

my_list= list(strings)
print(my_list)
print(type (my_list))

#Ahora ya podemos hacer cambios 
my_list[1] = 'juli'
print (my_list)

#Y la podemos volver a convertir a una tupla
my_tuple= tuple(my_list)
print(my_tuple)






