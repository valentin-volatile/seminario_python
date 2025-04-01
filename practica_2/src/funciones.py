import string
import random

def get_longest_title(titles):
	max_words = 0
	max_title = ""

	for title in titles:
		cant_words = len(title.split())
		if(cant_words > max_words):
			max_words = cant_words;
			max_title = title;
			
	return max_title
	

def search_matching_rules(rules, keyword):
	matching = []
	
	for rule in rules.split(".\n"):
		if(keyword in rule): matching.append(rule)
		
	return matching


def validate_username(username):
	#chequeo largo
	if(len(username)<5): return False 

	#chequeo numero
	only_numbers = "".join(char for char in username if char in "0123456789")
	if(len(only_numbers) == 0): return False 
		
	#chequeo mayuscula
	if(username.lower() == username): return False 
		
	#chequeo que sea alfanumerica
	if(not username.isalnum()): return False 

	return True


def get_keyword_count(descriptions, keywords):
	cant_dict = {}
	
	# inicializo de forma explicita cada par clave/valor
	for keyword in keywords:
		cant_dict[keyword.lower()] = 0;
	
	for desc in descriptions:
		words = desc.lower().split() # se pasa a minuscula y se separa en palabras
		for word in words:
			if word in cant_dict:
				cant_dict[word] += 1
				
	return cant_dict


def generate_discount_code(username, date, length = 30):
	valid_chars = string.ascii_uppercase + string.digits;
	
	code = username.upper() + '-' 
	code += "".join(c for c in date.split('-')) + '-';
	code += "".join(c for c in random.sample(valid_chars, k = length-len(code)))
	
	return code
	

def check_anagram(word1, word2):
	word1 = "".join(sorted(word1.lower()))
	word2 = "".join(sorted(word2.lower()))
	
	return word1 == word2


def remove_duplicates(clients):
	def make_key_from_name(name):
		name = name.lower()
		name = name.replace('á', 'a')
		name = name.replace('é', 'e')
		name = name.replace('í', 'i')
		name = name.replace('ó', 'o')
		name = name.replace('ú', 'u')
	
		return name
	
	# por el código ASCII, nombres con tilde quedan antes (al invertir el orden) que nombres iguales sin tilde
	clients.sort()
	clients.reverse()
	
	# creo copia de la lista para no eliminar mientras itero sobre la original
	clients_copy = clients[:]
	already_added = []
	
	for client in clients_copy:
		# elimino nombres repetidos de la lista original
		if(make_key_from_name(client) in already_added):
			clients.remove(client)
		else:
			already_added.append(make_key_from_name(client))
	
	clients.sort()
 
 
def remove_extra_spaces(clients):
	for i in range(len(clients)):
		if(type(clients[i]) is str): clients[i] = clients[i].strip();


def format_names(clients):
	for i in range(len(clients)):
		if(type(clients[i]) is str): clients[i] = clients[i].title();
	
	
def remove_empty_names(clients):
	# creo copia de la lista para no eliminar mientras itero sobre la original
	clients_copy = clients[:]
	
	for client in clients_copy:
		if(client is None or client.strip() == ""):
			clients.remove(client)
