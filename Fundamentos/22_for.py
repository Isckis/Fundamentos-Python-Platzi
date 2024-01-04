# for tendrá ciertas condiciones dadas, lo primero tiene un elemento iterador
# luego tenemos el in range, que hará un número de iteraciones hasta un número dado
'''for element in range (20):
    print(element)

# acá con esta estructura recorremos desde el 1 hasta el 20 a diferencia del anterior que recorrimos desde el 0
for element in range (1:20):
    print(element)
'''

# para recorrer esta lista usaremos for. Es importante recordar que element podría ser i, donde en este caso my_list es el range
my_list = [23, 45, 67, 89, 43]

for element in my_list:
    print (element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
    print (element)

#también podemos iterar diccionarios 

product = {
    'name': 'Camisa',
    'price':100,
    'stock':89
}

for element in product:
    print(element)

#si quisiera saber los valores tendría que hacerlo de la siguiente manera
for element in product:
    print (product[element])

#podríamos denominar el element por lo que es y que el resultado sea el atributo y su valor
for key in product:
    print (key, '=>', product [key])

# hay una forma rápida de hacerlo 
print (('*')*20)
for key, value in product.items():
    print (key, '=>', value)

print (('*')*20)
#Una de las formas de presentar la información más comunes será las listas de diccionario

people = [
    {
        'name': 'nico',
        'age': 34
    },

    {
        'name': 'zule',
        'age': 45
    },

    {
        'name': 'santi',
        'age': 4
    }
]

#acá el elemento de iteración podrías ser cualquiera, podría ser element, podría ser person
for person in people:
    print (person) 
    #también puedo iterar los valores específicos de las listas en el diccionario con los []
    print ('name =>', person['name'])
