#Calculadora científica:
#Para simular el funcionamiento de una calculadora científica, solicitar el ingreso de un número
#y mostrar un menu de operaciones disponible (seno, coseno, tangente, elevado al cuadrado y raíz cuadrada)
#Imprimir debajo el resultado luego de elegir la operación, repitiendo indefinidamente
#mientras el número del cálculo sea distinto de 0.
#Generar mensaje de error si el número de operación elegida no está en la lista.

import math
print ()
print ("Operaciones diponibles")
print ("1; seno")
print ("2; coseno")
print ("3; tangente")
print ("4; elevado al cuadrado")
print ("5; raiz cuadrada")
print ()

while (True):
    numeroAOperar = float(input("Ingresar número: "))
    if (numeroAOperar == 0):
        break

    else:
        tipoOperacion = int(input("Operación deseada: "))
    if (tipoOperacion == 1):
        print ("el seno de ",numeroAOperar, "es ",math.sin(numeroAOperar))
        print()
    elif (tipoOperacion == 2):
        print ("el coseno de ",numeroAOperar, "es ",math.cos(numeroAOperar))
        print()
    elif (tipoOperacion == 3):
        print ("la tangente de ",numeroAOperar, "es ",math.tan(numeroAOperar))
        print()
    elif (tipoOperacion == 4):
        print ("el cuadrado de ",numeroAOperar, "es ",numeroAOperar * numeroAOperar)
        print()
    elif (tipoOperacion == 5):
        print ("la raiz cuadrada de ",numeroAOperar, "es ",math.sqrt(numeroAOperar))
        print()
    else:
        print("Operación no válida")
    
print ()
print("Cálculos finalizados")
