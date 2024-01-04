x = 3.3 #3.3
print(x)

y = 1.1 + 2.2#3.30000000003
print(y)

#es interesante este ejemplo porque no dan lo mismo
print (x == y) #False

#le podmos quitar esa precisión décimal 
y_str=format(y, ".2g")
print ("str =>", y_str) #el problema es que queda convertida a String

###Acá tenemos hartos ejercicios posibles, me parece interesante, cómo volverlo 
#strings, en qué circunstancias necesitariamos eso? Para trabajar con divisas por ejemplo?
#O trabajar con conversiones?

#Ahora vamos a comparar el string de y con el string de x para que nos dé la igualdad
print (y_str == str(x))


print('*'*20)
#sin embargo no es una solución matemática
#si imprimimos ambos números nos damos cuentas que son iguales
#hasta cierto punto, por eso trabajaremos 
#una especie de tolerancia

print (y, x)
tolerance = 0.00001
print (abs (x - y) < tolerance)

#con Abs sacamos el valor absoluto, y al restarlos y compararlos 
#con esta tolerancia dejamos un margen de tolerancia 
#pues si fueran iguales nos daría 0, pero ahora le decimos que no sea 0
#sino que 0,00001 y si es menor entonces tenemos un hermoso True


