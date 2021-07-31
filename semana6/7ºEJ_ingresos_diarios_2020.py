
""" Cálculos sobre ingresos:
Se dispone de un reporte de ingreso diario del año 2020, en archivo de texto con formato CSV
(valores separados por coma), ver adjunto.

1. Cargar el paquete de reportes en una lista.
2. Calcular el promedio diario de ingresos del 1er semestre.
3. Calcular el promedio diario de ingresos del 2do semestre.
4. Calcular el promedio diario de ingresos de todo el año.
5. Calcular el % de días en el año, en los que se logró un ingreso mayor o igual a 8000.
6. Imprimir los 4 cálculos, y además el monto del día de mayor ingreso y el de menor ingreso. """

matIngDiario = [] #Inicializa o crea la lista vacía

ArchivoIngDiario = open("7ºEJ_ingresos_diarios_2020.txt", "r")
    #Creamos el objeto o variable ArchivoIngDiario importando la información desde un archivo
    #Abre el archivo de texto. La "r"determina que será para lectura,
    #Si ponemos "w" podría escribir sobre el archivo
matIngDiario = ArchivoIngDiario.read().split(",")
    #El comando read() nos permite leer el archivo, 
    #split(",") indica que las comas del archivo de texto separan lo valores de la lista
ArchivoIngDiario.close()
#print (matIngDiario) #Hasta aquí, los datos se importa como string.
print()
#Para convertirlos en enteres, utilizamos "for" con "enumerate", que crea un índice para cada ítem
# y en la linea siguiente, se convierte cada valor en entero
for indice , item in enumerate(matIngDiario):
    matIngDiario [indice]= int(item)
"""     if (indice<5): #Muestra solo los primeros 5 valores de la lista
        print (item) """
print(matIngDiario [0:7]) #Muestra valores del índice 0 al 7, uno a contiuación de otro

print()

cantDatos = (len(matIngDiario)) #La función "len" devuelve el tamaño de una lista
cantDiaPriSemtre = int((cantDatos/2)+1)
cantDiaSegSemtre = int(cantDatos-cantDiaPriSemtre)
print ("La cantidad total de días es ",cantDatos)
print("La cantidad de días del primer semestre es ",cantDiaPriSemtre)
print("La cantidad de días del segundo semestre es ",cantDiaSegSemtre)

sumaPriSemtre = 0
sumaSegSemtre = 0
sumaAnual = 0
promPriSemtre = 0
promSegSemtre = 0
promAnual = 0
diasIngMayor = 0

for indice , item in enumerate(matIngDiario):
    matIngDiario [indice]= int(item)
    sumaAnual = sumaAnual + item
    if (item>=8000):
        diasIngMayor = diasIngMayor + 1
        if (indice < cantDiaPriSemtre):
            sumaPriSemtre = sumaPriSemtre + item
        elif(indice >= cantDiaPriSemtre):
            sumaSegSemtre = sumaSegSemtre + item
    else:
        if (indice < cantDiaPriSemtre):
            sumaPriSemtre = sumaPriSemtre + item
        elif(indice >= cantDiaPriSemtre):
            sumaSegSemtre = sumaSegSemtre + item

relaDiasIngMayor = float(diasIngMayor/cantDatos)
promPriSemtre = int(sumaPriSemtre/(cantDiaPriSemtre))
promSegSemtre = int(sumaSegSemtre/cantDiaSegSemtre)
promAnual = int(sumaAnual/cantDatos)
print()
print("-------------------------------------------")
print(sumaPriSemtre, " ingresaron el primer semestre")
print(promPriSemtre," es el promedio de personas ingresadas durante los primeros",cantDiaPriSemtre," días")
print()
print(sumaSegSemtre, " ingresaron el segundo semestre")
print(promSegSemtre, "es el promedio de personas ingresadas durante el segundo semestre")
print()
print(sumaAnual, " ingresaron en todo el año")
print(promAnual, " es el promedio anual de ingresos")
print()
print("En ",diasIngMayor," días ingresaron mas de 8000 personas, lo que representa un ", "{:0.0%}".format(relaDiasIngMayor)," del total de días")
print("%0.3f"% (relaDiasIngMayor)) #imprime un número flotante de 3 decimales
print("{:0.3}%".format(relaDiasIngMayor)) #imprime un porcentaje de 3 decimales
print("{:0.2%}".format(relaDiasIngMayor)) #imprime un porcentaje de 2 decimales multiplicando x 100
print()


matIngDiario.sort(reverse=False)
print(matIngDiario[0]," es la menor cantidad ingresada")
print(matIngDiario[-1], " es la mayor cantidad ingresada")
print()