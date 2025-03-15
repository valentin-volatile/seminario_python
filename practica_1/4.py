import sys

nums = []
x = ''

while(not x.isnumeric() or (int(x) != 0)):
	x = input("Ingrese un número (0 para terminar): ")
	if(x.isnumeric() and (int(x) != 0)):
		nums.append(int(x))

print("Los números pares ingresados son: ")
for i in nums:
	if(i%2): continue
	print(i)

