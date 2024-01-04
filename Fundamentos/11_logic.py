# and

print ('And')
print ('True and True =>', True and True)
print ('True and False =>', True and False)
print ('False and True =>', False and True)
print ('False and False=>', False and False)

print ('*'*20)

print (10 > 5 and 5 > 10)
print (10 > 5 and 5 > 10)

#Acabamos de aplicar operadores de comparación con el operador and  
#Ahora lo que necesitamos es comprobar si un input que por defecto es string 
#convertido a un int 
stock = input ('Ingrese el número de stock =>')
stock = int (stock)

#Para luego saber si cumple con la regla de nuestro programa 
print (stock >= 100 and stock <=1000)

###Sería interesante generar antes de pasar a los If programas que puedan identificar verdaderos o falsos

print ('*'*20)

#OR

print ('Or')
print ('True or True =>', True or True)
print ('True or False =>', True or False)
print ('False or True =>', False or True)
print ('False or False=>', False or False)


print ('*'*20)

role = input ('Digita el rol =>')

print (role == 'admin' or role == 'seller')
 
 # de esta forma verificamos usuarios en un programa para poder continuar. 
###se podría utilizar para verificar usuarios dentro de un juego, o parámetros, viste un triángulo o un cuadrado, tipo test de rocha. 