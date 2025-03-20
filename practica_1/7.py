nums = []
user_input = ''

while(True):
	user_input = input("Ingrese un número entero (0 para terminar): ")
	
	if((user_input[0] == '-' and user_input[1::].isnumeric()) or user_input.isnumeric()):
		user_input = int(user_input)
		if(user_input == 0): break
		nums.append(user_input)
	
cadena = ("".join(str(i)+"-" for i in nums if i%3 != 0))[:-1] #slice al final para eliminar el último -
print(cadena) #negativos quedan como --x, sigue la consigna
