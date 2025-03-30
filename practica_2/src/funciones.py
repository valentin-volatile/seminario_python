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


def clean_client_list(clients):
	# set para evitar repetidos
	clean_list = set()
	
	for client in clients:
		# no agrego None
		if(client == None): continue;
		
		client = client.strip()
		# no agrego string vacía
		if(client == ""): continue;
		
		# pongo primera letra de cada palabra en mayus
		client = string.capwords(client);
		
		clean_list.add(client);
	
	return sorted(clean_list)
