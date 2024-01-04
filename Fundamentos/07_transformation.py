name = 'Nicolas'
print (type (name))
name = 12
print (type (name))
name = True
print (type(name))

print ("Nicolas" + "Molina")
print (10 + 20)
# print ("Nicolas" + 20) Este caso da error no se pueden sumar int + string
# por eso es importante igualarlos 
print ("Nicolas" + "20")


#Ahora con str() transformamos un int a str
age = 12
# transformamos a str
print ("Mi edad es" + str(age)) 
#con la función format "f" al usar las llaves {} entiende que todo 
#será utilizado como string 
print (f" Mi edad es {age}")

#ahora le preguntamos al usuario
age = input ('Escribe tu edad =>')
print(type (age))
print(f'Tu edad en 10 años será {age}')

#ahora tenemos una variable string porque input recibe todo como string 
#entonces transformamos la respuesta del usuario a int

age = input ('Escribe tu edad =>')
print(type (age))
#transformamos a int
age = int (age) 
age += 10
print(f'Tu edad en 10 años será {age}')



