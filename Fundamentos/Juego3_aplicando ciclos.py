"""Por algún motivo no funciona en visualcode pero sí en replit, porqué!"""



#aplicaremos los ciclos para que se cuenten las victorias y después de un número de victorias se de un ganador
import random

options = ('piedra', 'papel', 'tijera')

#para que nuestro ciclo no sea infinito tendremos un contador: Rondas
rounds = 1

#haremos variables para contar las victorias
computer_wins = 0
user_wins = 1


#por eso después de definir nuestras opciones, deberíamos generar ese loop 
#para que el juego repita hasta que se cumpla la condición de ganar, por lo que al 
#poner el while tardíamente en nuestro código tenemos que shiftearlo hacia la derecha una posición
while True: 

    #al principio de nuestro juego se llevará el contador de en qué posición vamos
    print (('*')*20)
    print('ROUND', rounds)
    print (('*')*20)

    print ('computer_wins', computer_wins)
    print ('user_wins', user_wins)

    #interesante probar hasta aquí, pues jugaremos hasta el infinito, hay que definir el contador de round al final

    user_option = input ('piedra, papel o tijera =>')
    user_option = user_option.lower()
    rounds += 1

    if not user_option in options:
        print('esa opción no es valida')
        #con esto haremos que nuestro juego cuente las opciones inválidas, por eso subimos los rounds antes 
        #del continue para que pueda contar los rounds de las opciones inválidas
        continue
        
    computer_option = random.choice (options)

    print ('User option =>', user_option)
    print ('computer option =>', computer_option)
   
    if user_option == computer_option:
        print('Empate!')

    elif user_option == 'piedra':#opción 1 con sus dos posibilidades
        if computer_option == 'tijera':
            print ('piedra gana a tijera')
            print ('user ganó')
            #sumaremos +1 al contador de user y sucesivamente al de computer
            user_wins+=1
        else:
            print ('papel gana a piedra')
            print ('computer ganó')
            computer_wins+=1

    elif user_option == 'papel':#opción 2 con sus dos posibilidades
        if computer_option == 'piedra':
            print ('papel gana a piedra')
            print ('User ganó')
            user_wins+=1

        else:
            print ('tijera gana a papel')
            print ('computer ganó')
            computer_wins+=1

    elif user_option == 'tijera':#opción 3 con sus dos posibilidades
        if computer_option == 'papel':
            print ('tijera gana a papel')
            print ('el usuario ganó')
            user_wins+=1
        else: 
            print ('piedra gana a tijera')
            print ('computer ganó')
            computer_wins+=1
    
    if computer_wins ==2:
        print('El ganador es la computadora')
        break
    if user_wins ==2:
        print('El ganador es el usuario')
        break
    
    
    