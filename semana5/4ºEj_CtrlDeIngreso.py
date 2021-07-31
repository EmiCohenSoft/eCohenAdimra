# Control de ingreso:
# En una sala de juegos, se debe cobrar un ingreso de manera diferenciada según la edad del cliente.
# Si la persona tiene hasta 8 años inclusive, ingresa gratis; 
# si tiene hasta 17 inclusive, debe pagar $ 100.00, y de allí en adelante $ 200.00.
# Escribir un programa que solicite indefinidamente edades, hasta que se ingrese un 0, 
# en ese momento debe finalizar y mostrar en pantalla cuántos de cada grupo han ingresado,
# el subtotal cobrado del grupo (salvo el gratuito, lógicamente), y el total general.

EDAD_NINIO = 8
EDAD_JOVEN = 17

TARIFA_JOVEN = 100
TARIFA_ADULTO = 200

edad = -9999
niniosIng = 0
jovenesIng = 0
adultosIng = 0
recaudaJovenes=0
recaudaAdulto=0

while (edad !=0):
    edad = int(input("Ingrese la edad:"))
    print(edad)
    if (0 < edad <= EDAD_NINIO):
            niniosIng = niniosIng + 1
    if (EDAD_NINIO < edad <= EDAD_JOVEN):
            jovenesIng = jovenesIng + 1
            recaudaJovenes = recaudaJovenes + TARIFA_JOVEN
    if (edad > EDAD_JOVEN):
            adultosIng = adultosIng + 1
            recaudaAdulto = recaudaAdulto + TARIFA_ADULTO
    
print("Han ingresado ",niniosIng, " niños")
print("Han ingresado ",jovenesIng, " jovenes, con una recaudación de: ", recaudaJovenes)
print("Han ingresado ",adultosIng, " adultos, con una recaudación de: ", recaudaAdulto)
print("Recaudación total: ", recaudaJovenes+recaudaAdulto)
    