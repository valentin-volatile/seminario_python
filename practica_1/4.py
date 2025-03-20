nums = []
user_input = ''

while(not user_input.isnumeric() or (int(user_input) != 0)):
	user_input = input("Ingrese un número entero positivo (0 para terminar): ")
	if(user_input.isnumeric() and (int(user_input) != 0)):
		nums.append(int(user_input))

nums_pares = [num for num in nums if num%2 == 0]
print("Los números pares ingresados son: ")
for i in nums_pares:
	print(i)
