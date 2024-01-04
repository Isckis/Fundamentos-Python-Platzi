#INDEXING

text = 'Ella sabe python'
print (text[0])
#Esta indicación nos devolverá el primer carácter en esta posición (E)
print (text [1])
#print (text [999]) Esto nos tirará error pues no existe 

#Para ver el último carácter podemos uasar len, para saber el tamaño del texto y así poner el último carácter

size = len(text)
#print (text [size])
print('size =>', size)

#Hasta aquí lanza un error, pues len cuenta la cantidad de carácteres por lo que tenemos un 16, pero la posición 16
#no existe pues el rango va desde 0 a 15, por lo que hay que decirle:

print(text[size -1])

#python hace las cosas más fáciles pues no es necesario hacer el cálculo de len y restarle -1 sino que podemos 
#restar 1 inmediatamente

print(text[-1])

#ojo con los espacios en el text "ella sabe python " hay un espacio alfinal, por lo que al principio me lanzaba
#un resultado fantasma

#SLICING
#con este comando lo que logramos es que la terminal devuelva un rango específico

print (text [0:5])
print (text[10:16])

#si al principio del rango no tienes nada, python la reconocerá como 0

print (text[:10])

#ahora bien, si queremos ir al final le pedimos podríamos uasar el -1
print (text [5:-1])

#pero como vemos no imprime el último carácter, por lo que tenemos esta otra forma
print (text [5:])

#esta sintaxis irá desde el inicio al final
print (text[:])

#están los saltos, está el primer parámetro del rango, luego tenemos la indicación de que salte
print (text [10:16:1])
print (text [10:16:2])
print (text [::2])




