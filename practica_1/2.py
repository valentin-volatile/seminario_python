import sys

def celsius_to_fahrenheit(x):a
	return ((x*9)/5)+32

temp = ''
while(not temp.isnumeric()):
	temp = input("Ingrese temperatura en celsius: ")

print(temp, "°C", "es equivalente a", celsius_to_fahrenheit(float(temp)), "°F")
