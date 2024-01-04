#la matriz es una lista que tiene listas adentro

matriz = [
    [1,2,3],
    [4,5,6], 
    [7,8,9]
    ]

#la siguiente instrucción nos devuelve [1, 2, 3]
print (matriz[0])

#pero podemos trabajar con coordenadas preguntarle qué está en la posición [0] [1] lo que no da resultado 2
print (matriz [0][1])

#ahora veremos los ciclos anidades, es importante que el element cambie de nombre en cada ciclo anidado para que no
#choquen
for element in matriz:
    print (element)
    for item in element:
        print(item)

print (('*')*20)

#si nos fijamos en el ejemplo anterior el element es la fila (row) y el item es la columna (columnt) por lo que podemos:

for row in matriz:
    print (row)
    for column in row:
        print(column)
