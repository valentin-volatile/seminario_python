def get_longest_title(titles):
	max_words = 0
	max_title = ""

	for title in titles:
		cant_words = len(title.split())
		if(cant_words > max_words):
			max_words = cant_words;
			max_title = title;
			
	return max_title
