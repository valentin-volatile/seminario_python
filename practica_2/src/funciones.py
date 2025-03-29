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
