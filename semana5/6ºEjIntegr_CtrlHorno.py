# Importación de librería función random para la generación aleatoria de números
import random

#Definición de constantes
LIMITE_TEMP_MIN = 100
LIMITE_TEMP_MAX = 200
TOLERANCIA = 2
CANT_DE_LECT = 10

#Definición de variables
tempDePrueba = -9999
numeroDeLectura = 0
mensaje = "Ingresar temperatura de prueba entre " + str(LIMITE_TEMP_MIN) + " y " + str(LIMITE_TEMP_MAX) + ": "

# Ciclo principal, se genera aleatoriamente la temperatura objetivo del horno
while(True):
        sumaDeLect = 0
        tempObjetivo = (random.randint(LIMITE_TEMP_MIN,LIMITE_TEMP_MAX))
        print ()
        print ("----------------------------------------------------")
        print ("CONTROL DE ENCENDIDO DEL QUEMADOR")
        print ()
        print ("Temperatura objetivo: ",tempObjetivo)
        print ()

#Se solicita ingreso de una temperatura simulada de ensayo
#        print("Ingresar temperatura de prueba entre ",(LIMITE_TEMP_MIN)," y ",(LIMITE_TEMP_MAX),": ")
#        tempDePrueba = int(input("  "))
        tempDePrueba = int(input(mensaje))
        print()


#Condición que limita la que temperatura ingresada manualmente esté dentro del rango de control
        if (tempDePrueba != 0):
#Condición que ejecutará el ciclo si el valor ingresado por consola es distinto de cero
            if (LIMITE_TEMP_MIN <= tempDePrueba <= LIMITE_TEMP_MAX):
#Ciclo que genera lecturas aleatoreas simuladas, próximas a la ingresada por consola dentro de la tolerancia.
#No utilicé la temperatura objetivo porque de esa manera siempre sería un horno estable
                    for ciclo in range(CANT_DE_LECT):
                        lectSensor = (random.randint(tempDePrueba-TOLERANCIA, tempDePrueba+TOLERANCIA))
                        numeroDeLectura = numeroDeLectura + 1
                        sumaDeLect = sumaDeLect + lectSensor
                        print ("Temperatura sensada: ",lectSensor, "Lectura ",numeroDeLectura, "/",CANT_DE_LECT)
#Cálculo de la lectura promedio
                    promLect = int(sumaDeLect/CANT_DE_LECT)
                    print("Lectura promedio: ",promLect)
#Condición que coteja el promedio contra la temperatura objetivo y muestra el mensaje de resolución
                    if (promLect<tempObjetivo-TOLERANCIA):
                        print()
                        print("   Temperatura baja, se enciende quemador")
                    elif (promLect > tempObjetivo+TOLERANCIA):
                        print()
                        print("   Temperatura alta, se apaga quemador")
                    else:
                        print()
                        print("   Horno estable")
#Mensaje de error en caso que la temperatura ingresada por consola está fuera de rango
            else:
                print("Temperatura fuera de rango. Reingresar temperatura")
                print()
                #Condición que detendrá el ciclo si el valor ingresado por consola es cero
        else:
            print ("CONTROL FINALIZADO")
            print ()
            break
