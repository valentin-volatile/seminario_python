operaciones = [
	"Agregar un nuevo producto", 
	"Eliminar un producto existente", 
	"Mostrar el inventario actual", 
	"Salir"
]

inventario = dict()
separador = "######################################"

while(True):
	print(separador)
	print("Seleccione una acción para realizar:\n")
	for i, prompt in enumerate(operaciones):
		print(f"{i+1}. {prompt}")
	print(separador)
	
	# Se intenta registrar la elección del usuario, valores no válidos son manejados por el wildcard del match
	try: op = int(input())
	except ValueError: pass

	match op:
		case 1:
			nombre = input("Ingrese el nombre del producto a agregar: ")
			try : cant = int(input("Ingrese la cantidad inicial: "))
			except ValueError:
				print("Cantidad no válida. No se realizaron cambios\n")
				continue
				
			if(nombre in inventario):
				print("El producto ingresado ya existe en el inventario. No se realizaron cambios\n")
			else:
				inventario[nombre] = cant
				print(f"El producto \"{nombre}\" fue agregado correctamente\n")
		case 2:
			nombre = input("Ingrese el nombre del producto a eliminar: ")
			if(nombre in inventario):
				del inventario[nombre]
				print(f"El producto \"{nombre}\" fue eliminado del inventario\n")
			else:
				print("El producto ingresado no existe en el inventario. No se realizaron cambios\n")
		case 3:
			print("\nInventario (producto, cantidad): ")
			for nombre, cantidad in inventario.items():
				print(f"\"{nombre}\": {cantidad}")
			print()
		case 4:
			exit("Programa terminado por el usuario")
		case _: 
			print("Elección no valida, intente de nuevo\n")
