#condicionales, si condicionamos un programa a un True se ejecutará, pero jamás ejecutará un False

if True: 
    print ('debería ejecutarse')

if False:
    print ('nunca se ejecuta')

print ('*'*20)

"""
Lo comentamos porque lo desarrollaremos mas abajo

pet = input ('cuál es tu mascota favorita?')

if pet == 'perro':
    print ('genial tienes buen gusto')

if pet == 'gato':
    print ('espero tengas suerte')
"""

print ('*'*20)

# ahora veremos el if en relación al ejercicio que hicimos antes
stock = int (input ('Ingrese el número de stock =>'))

if stock >= 100 and stock <= 1000:
    print ('el stock es correcto')
else:
    print ('el stock es incorrecto')

print ('*'*20)

pet = input ('cuál es tu mascota favorita?')

#siguiendo con el ejemplo anterior podemos concatenar los if con elif y terminar con un else
#para hacer una diferencia de condicionales ###Investigar porqué usar if and elif
if pet == 'perro':
    print ('genial tienes buen gusto')

elif pet == 'gato':
    print ('espero tengas suerte')

elif pet == 'pez':
    print ('eres lo máximo')
else:
    print ('no tienes mascotas')

print ('*'*20)

#número par o impar

number = input('digita un número')
number = int (number)

if (number %2) == 0:
    print ('tu número es par')
else: 
    print ('tu número es impar')

###podríamos generar un else que devuelva a la pregunta, pero al parecer no se puede, le pregunté a GPT 
    #y me dió dos altenrativas una fue con while y la otra con funciones, y recomendó no hacerlo con condicionales pues 
    #el código sería muy enredado, sin embargo me lo dió igual acá van las tres versiones

    """
    #WHILE
    while True:
    pet = input('Cuál es tu mascota favorita? ')

    if pet == 'perro':
        print('¡Genial, tienes buen gusto!')
        break  # Sale del bucle si la respuesta es válida

    elif pet == 'gato':
        print('Espero que tengas suerte.')
        break  # Sale del bucle si la respuesta es válida

    elif pet == 'pez':
        print('Eres lo máximo.')
        break  # Sale del bucle si la respuesta es válida

    else:
        print('Respuesta no válida. Inténtalo de nuevo.')

            #En este código, se utiliza un bucle while que se ejecutará mientras 
                #la respuesta del usuario no esté en la lista de respuestas válidas. 
                #Si la respuesta no es válida, se imprime un mensaje y se vuelve a solicitar 
                #la entrada del usuario. Una vez que se ingresa una respuesta válida, el programa 
                #sale del bucle y continúa con la lógica de if-elif-else para imprimir el mensaje 
                #correspondiente.

    #DEF (funciones)
    def preguntar_mascota():
    pet = input('Cuál es tu mascota favorita? ')

    if pet in ['perro', 'gato', 'pez']:
        if pet == 'perro':
            print('¡Genial, tienes buen gusto!')
        elif pet == 'gato':
            print('Espero que tengas suerte.')
        elif pet == 'pez':
            print('Eres lo máximo.')
    else:
        print('Respuesta no válida. Inténtalo de nuevo.')
        preguntar_mascota()

    # Llamamos a la función para iniciar el proceso
    preguntar_mascota()

    ## Entiendo, si deseas evitar el uso de un bucle while, podrías usar una función recursiva para lograr el mismo resultado. Aquí tienes un ejemplo:

    #IF

    pet = input('Cuál es tu mascota favorita? ')

if pet == 'perro':
    print('¡Genial, tienes buen gusto!')
else:
    if pet == 'gato':
        print('Espero que tengas suerte.')
    else:
        if pet == 'pez':
            print('Eres lo máximo.')
        else:
            print('Respuesta no válida. Inténtalo de nuevo.')
            pet = input('Cuál es tu mascota favorita? ')
            
            if pet == 'perro':
                print('¡Genial, tienes buen gusto!')
            else:
                if pet == 'gato':
                    print('Espero que tengas suerte.')
                else:
                    if pet == 'pez':
                        print('Eres lo máximo.')
                    else:
                        print('Respuesta no válida. Has agotado tus intentos.')

        ##Este código utiliza anidamiento de condicionales para simular un bucle sin realmente usar uno. Sin embargo, ten en cuenta que este enfoque no es recomendado en situaciones reales, ya que dificulta la lectura del código y su mantenimiento. La utilización de bucles y funciones proporcionaría una solución más elegante y comprensible.




    """
