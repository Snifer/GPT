import webbrowser

def search(peticion):
	google =  "https://www.google.com/?#q="+ peticion
	bing = "https://www.bing.com/search?q="+ peticion
	duckgo = "https://duckduckgo.com/?q="+ peticion
	list = [google,bing,duckgo]
	for item in list:
		webbrowser.open(item)


if __name__ == "__main__":
	print """ 

|     |---------------------------|     |
|     |                           |     |
|-----| Bing, Google & DuckDuckGo |-----|
|     |          Hacking          |     |
|     |---------------------------|     |

	""" 
	while True:
		busqueda = raw_input("Copia tu Dork favorito: ")
		search(busqueda)