nums = []
user_input = ''

while(True):
	user_input = input("Ingrese un número (0 para terminar): ")
	if((user_input[0] == '-' and user_input[1::].isnumeric()) or user_input.isnumeric()):
		user_input = int(user_input)
		if(user_input == 0): break
		nums.append(user_input)

print("Los números ingresados son: ")
for num in nums:
	if(num<0): break
	print(num)

