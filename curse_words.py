import urllib
def read_text():
	quotes = open("/home/lokesh1729/MovieLibrary/movie_quotes.txt")
	content = quotes.read()
	print(content)
	check_profanity(content)
	quotes.close()
	
def check_profanity(check_text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?"+check_text)
	output = connection.read()
	print(output)
	connection.close()

read_text()
