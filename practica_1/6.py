import sys

nums = []
x = ''

while(True):
	x = input("Ingrese un número (0 para terminar): ")
	try: x = int(x)
	except ValueError: continue
	
	if(x == 0): break;
	nums.append(x)
	

pares = [i for i in nums if i%2 == 0]
impares = [i for i in nums if i%2 == 1]

print("Los números pares ingresados son: ")
print(pares)
print("Los números impares ingresados son: ")
print(impares)
