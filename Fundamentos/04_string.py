name = "Isaías"
last_name ="Castro"
print(name)
print(last_name)
full_name =name+last_name

#cómo agregar un espacio
full_name =name+" "+last_name
print(full_name)

#es importante que comilla doble y comilla sencilla nos sirven cuando una estará dentro del texto y queremos que sea parte del string
quote = "I' am Isaías"
print (quote)
quote2 = 'she said "hello"'
print (quote2)
#formato
template = "Hola, mi nombre es " + name + "y mi apellido es " + last_name
print ('v1',template)
template = "Hola, mi nombre es {} y mi apellido es {}".format (name, last_name)

print ('v2',template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print ('v3',template)