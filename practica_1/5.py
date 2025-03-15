import sys

nums = []
x = ''

while(True):
	x = input("Ingrese un número (0 para terminar): ")
	
	try: x = int(x)
	except ValueError: continue
	
	if(x != 0): nums.append(x)
	else: break

print("Los números ingresados son: ")
for i in nums:
	if(i<0): break
	print(i)

