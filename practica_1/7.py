import sys

nums = []
x = ''

while(True):
	x = input("Ingrese un número entero (ENTER o no entero para terminar): ")
	try: x = int(x)
	except ValueError: break
	
	nums.append(x)
	
cadena = ("".join(str(i)+"-" for i in nums if i%3 != 0))[:-1] #slice al final para eliminar el último -
print(cadena) #negativos quedan como --x, sigue la consigna
