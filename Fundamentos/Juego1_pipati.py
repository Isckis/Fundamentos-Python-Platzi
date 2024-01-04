#generamos 2 variables para las elecciones del usuario y compu

#pondremos la respuesta del usuario en minúscula
#user_option = (input ('piedra, papel o tijera =>')).lower()
#otra opción sería agregar una línea }
user_option = input ('piedra, papel o tijera =>')
user_option = user_option.lower()
computer_option = 'piedra' #de momento compu tendrá una opción fija

#armamos la estructura de nuestro programa
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