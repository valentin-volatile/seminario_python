edad = ''

while(not edad.isnumeric()):
	edad = input("Ingrese su edad: ")
	
print("Le falta", 100-int(edad), "años para alcanzar los 100")
