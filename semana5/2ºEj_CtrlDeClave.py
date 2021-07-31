clinterna = "123Abcde"
LIMITE_INTENTOS = 2
usuarioValidado = False
numeroIntento = 0

for numeroIntento in range (LIMITE_INTENTOS):
  clave = input("ingresar clave: ")
  if(clave==clinterna):
      usuarioValidado = True
      print("clave correcta")
      break
  else:
    numeroIntento=numeroIntento+1
    print("clave incorrecta, Intento ",numeroIntento,"/", LIMITE_INTENTOS)

if (usuarioValidado == True):
  print ("SISTEMA OK")
else:
  print("SISTEMA BLOQUEADO")

# Probemos los cambios en Git