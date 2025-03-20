nums = []
user_input = ''

while(not user_input.isnumeric() or (int(user_input) != 0)):
	user_input = input("Ingrese un número entero positivo (0 para terminar): ")
	if(user_input.isnumeric() and (int(user_input) != 0)):
		nums.append(int(user_input))

pares = [i for i in nums if i%2 == 0]
impares = [i for i in nums if i%2 == 1]

print("Los números pares ingresados son: ")
print(pares)
print("Los números impares ingresados son: ")
print(impares)
