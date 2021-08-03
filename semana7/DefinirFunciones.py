apellido = ""
nombre = ""

def formatearNombre():
	nombreFormateado = apellido.upper() + ", " + nombre.capitalize()
	print(nombreFormateado)

for ciclo in range(2):
	apellido = input("Ingresar apellido: ")
	nombre = input("Ingresar nombre: ")
	
	formatearNombre()