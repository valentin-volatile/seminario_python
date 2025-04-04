import string
import random

# Ejercicio 2
def get_longest_title(titles):
	max_words = 0
	max_title = ""

	for title in titles:
		cant_words = len(title.split())
		if(cant_words > max_words):
			max_words = cant_words;
			max_title = title;
			
	return max_title
	

# Ejercicio 3
def search_matching_rules(rules, keyword):
	matching = []
	
	for rule in rules.split(".\n"):
		if(keyword in rule): matching.append(rule)
		
	return matching


# Ejercicio 4
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


# Ejercicio 6
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


# Ejercicio 7
def generate_discount_code(username, date, length = 30):
	valid_chars = string.ascii_uppercase + string.digits;
	
	code = username.upper() + '-' 
	code += "".join(c for c in date.split('-')) + '-';
	code += "".join(c for c in random.sample(valid_chars, k = length-len(code)))
	
	return code


# Ejercicio 8
def check_anagram(word1, word2):
	word1 = "".join(sorted(word1.lower()))
	word2 = "".join(sorted(word2.lower()))
	
	return word1 == word2


# Ejercicio 9
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


# Ejercicio 10
def get_blank_score_data(ronda):
	players = list(ronda.keys())
	fields = ["kills", "assists", "deaths", "cant_MVP", "score"]
	score_data = {}
	
	for player in players:
		score_data[player] = {}
		for field in fields:
			score_data[player][field] = 0
	
	return score_data


def update_scores(score_data, ronda, kill_value=3, assist_value=1, death_value=-1):
	values = {"kills": kill_value, "assists": assist_value, "deaths": death_value}
	
	# para posterior cálculo de MVP
	points_earned = {}
	
	for player, actions in ronda.items():
		points = 0
		
		for action, cant in actions.items():
			score_data[player][action] += cant
			points += cant*values[action];
		
		points_earned[player] = points;
		score_data[player]["score"] += points
	
	MVP = max(points_earned, key = lambda player:points_earned[player])
	
	score_data[MVP]["cant_MVP"] += 1


def print_scores(score_data):
	# obtengo jugadores y los ordeno según sus puntos
	players = list(score_data.keys())
	players.sort(key=lambda player:score_data[player]["score"], reverse=True)
	
	largo = 18 # lo que mide cada "celda" en caracteres, número arbitrario
	column_titles = ["Jugador", "Kills", "Asistencias", "Muertes", "MVPs", "Puntos"]
	separador = "-"*(len(column_titles)*largo)
	
	
	print(separador)
	for title in column_titles:
		print(f"{title:^{largo}}", end="") # ^x -> centra la string, que ocupa x caracteres
	print("\n"+separador)
	
	for player in players:
		print(f"{player:^{largo}}", end="")
		for value in score_data[player].values():
			print(f"{value:^{largo}}", end="") 
		print()
	print()
