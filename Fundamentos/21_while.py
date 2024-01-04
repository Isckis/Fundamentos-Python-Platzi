
# le damos una condición if, y se ejecuta la acción
if True:
    print('se ejecutó')

#while es un comando que se ejecutará hasta o durante se cumpla una condición
#acá estamos frente a un ciclo infinito, en el if se ejecuta una vez, acá infinito (ctrl+c) se detiene el programa
''' 

while True:
   #print('se ejecutó')

counter = 0 

while counter < 10:
    counter +=1
    print(counter)
    

counter = 0 

while counter < 20:
    counter += 1
    #pero si por alguna razón quiero romper el ciclo puedo usar break y se usa de la siguiente forma
    if counter == 15:
        break
    print (counter)

'''
# ya vimos break, pero también tenemos continue, que repite el ciclo hasta que la sentencia 
#previa al continue no se cumpla 

counter = 0 

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print (counter)
