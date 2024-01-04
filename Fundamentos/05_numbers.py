lives = 3
print (type(lives))

age = 12
buget = 100

temperature =12.12
print (type(temperature))

lives = 2 
print (lives)
lives = 1
print (lives)

lives = 12 + 15 
print (lives)

lives = lives - 1 
print (lives)

lives -= 1
print (lives)

#Abreviatura python para operaciones matemáticas (+,-,*,/)=

number = 45000000000000000.1
print (number)

number_b = 0.00000000000001
print (number_b)

"""
programa que calcule el promedio de los gastos de ciertos meses, 
3 variables, presupuesto de cada mes (presupuesto enero, febrero, 
marzo, promedio)
"""
presupuesto_enero = 1000
presupuesto_febrero=2000
presupuesto_marzo = 3000

promedio = (presupuesto_enero+presupuesto_febrero+presupuesto_marzo)/3
print(promedio)

#opción 2

pres_enero= input ("asigne un presupuesto para enero")
pres_febrero= input ("asigne un presupuesto para febrero")
pres_marzo= input ("asigne un presupuesto para marzo")

promedio = (int(pres_enero)+int(pres_febrero)+int(pres_marzo))/3

 
print (f"El promedio para el presupuesto para los tres meses es {promedio}")


