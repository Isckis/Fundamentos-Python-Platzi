"""
En este desafío, se te proporcionará un código base encontrarás las variables 
name y age todas como strings. 
Tu tarea es crear un formato de string que, como resultado, muestre un mensaje 
en la sección Terminal. El mensaje deberá tener la siguiente forma:

Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años

Ten en cuenta que debes calcular la edad que tendrás en 10 años a partir de 
la edad. Por ejemplo, si la edad es 29 años, el mensaje mostrado deberá decir
 "tengo 29 años y en 10 años tendré 39 años"
"""
name = 'Juana'
print(name)
age = '10'
age = int(age)
print(age)
total = age + 10



template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años"
print(template)