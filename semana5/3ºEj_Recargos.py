mayoriaEdad = 18
declaJurIngreso = 20000
precioPrdto = 3500
alicuota = 0.15

while (True):

  edad = int(input ("Su edad es: "))
  ingresos = int(input ("Su declaración jurada de ingresos es: "))
  if (edad >= mayoriaEdad):
    if (ingresos >= declaJurIngreso):
      gravamen = precioPrdto * alicuota
      precioFinal = precioPrdto + gravamen
      print ("Su compra está gravada")
    else:
      gravamen = 0
      precioFinal = precioPrdto
      print ("Su compra no será gravada")
    
  else:
    gravamen = 0
    precioFinal = precioPrdto
    print ("Su compra no será gravada")

  print ("precio Final: ",precioFinal, "Gravamen: ",gravamen)
  print ()