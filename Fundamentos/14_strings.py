text = 'Ella sabe programar en Python'

#tenemos este texto con IN buscamos si hay un elemento en una línea de código

print ('JavaScript' in text)#False

print ('Python' in text) #True

#Con lenn examinamos el tamaño de un string

size = len ('amor')
print (size)

#no ponemos text entre comillas pues estamos contando la variable
size=len(text)
print (size) 

print (text)
print (text.upper())
print(text.lower())
print (text.count('a'))

text_2='este es un título'
print (text_2)
print(text_2.capitalize())
print (text_2.title())
print (text_2.isdigit())

print('389'.isdigit())