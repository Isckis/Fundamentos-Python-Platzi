# En esta evolución del juego aplicaremos las tuplas, nos viene súper bien, pues nuestras opciones no cambiarán

#importaremos la función Random para que la computadora de soluciones aleatorias
#random.choice (options) dentro de la tupla que creamos
import random

#primero creamos las opciones del juego con una tupla
options = ('piedra', 'papel', 'tijera')

user_option = input ('piedra, papel o tijera =>')
user_option = user_option.lower()

#podemos dar una respuesta a opción invalida
if not user_option in options:
    print('esa opción no es valida')
    
computer_option = random.choice (options)

print ('User option =>', user_option)
print ('computer option =>', computer_option)
if user_option == computer_option:
    print('Empate!')

elif user_option == 'piedra':#opción 1 con sus dos posibilidades
    if computer_option == 'tijera':
        print ('piedra gana a tijera')
        print ('user ganó')
    else:
        print ('papel gana a piedra')
        print ('computer ganó')

elif user_option == 'papel':#opción 2 con sus dos posibilidades
    if computer_option == 'piedra':
        print ('papel gana a piedra')
        print ('User ganó')

    else:
        print ('tijera gana a papel')
        print ('computer ganó')

elif user_option == 'tijera':#opción 3 con sus dos posibilidades
    if computer_option == 'papel':
        print ('tijera gana a papel')
        print ('el usuario ganó')
    else: 
        print ('piedra gana a tijera')
        print ('computer ganó')