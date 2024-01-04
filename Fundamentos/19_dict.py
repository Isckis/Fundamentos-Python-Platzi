#los diccionarios son una estructura de datos que se reconoce por los corchetes en los que definimos
#clave:valor

my_dict={}

print(type(my_dict))

my_dict = {
    'avion': "bla bla bla",
    'name': "Nicolas",
    'last_name': "Molina Monroy",
    'age': 87
}

print (my_dict)

#podemos saber cuántos elementos hay en este diccionario
print(len (my_dict))

#con los corchetes cuadrados podemos interrogar a las llaves sobre su valor
print (my_dict ['age'])
print (my_dict ['last_name'])

#también puedo obtener con este otro metodo, y en el caso que no existiera el valor,  como unvalor, 
#me devuelve None, me sirve en el caso de que no esté tan seguro de que un diccionario no tenga una llave
print (my_dict.get('age'))
print (my_dict.get('unvalor'))

#otra forma de saberlo es preguntándole específicamente por la llave, si está dará True y sino está dará False
print('avion' in my_dict)
print('otroqueno' in my_dict)

