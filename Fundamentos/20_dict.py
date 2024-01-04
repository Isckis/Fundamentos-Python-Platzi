#vamos a ver cómo poder trabajar y cambiar elementos de diccionarios

person = {

    'name': 'nico',
    'last_name': 'molina',
    'langs': ['python', 'javascript'],
    'age':99
}

print (person)

# podemos actualizar datos con los corchetes cuadrados
person ['name'] = 'santi'

# también puedo restarle a un atributo
person ['age'] -= 50

#puedo usar .append() para agregar elementos
person ['langs'].append('rust')
print (person)

#también podemos eliminar claves
del person['las_name']

#podemos usar pop en los diccionarios, pero acá a diferencia de las listas, si no le ponemos el elemento lanzará erros, a 
#diferencia de las listas que eliminaba el último elemento
person.pop('age')

#tenemos otras herramientas para trabajar con diccionarios .items() .keys() .values()
#Lo que hace el comando .item() es entregarme las keys y values en  pares de dupla, esto será muy útil cuándo 
#luego recorramos los diccionarios
print ('items')
print(person.items())

#cuándo solicitamos .keys() nos dará las listas o atributos
print ('keys')
print(person.keys())

#.values() nos envía una lista con los valores
print ('values')
print(person.values())


