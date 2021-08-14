from bs4 import BeautifulSoup
f = open("index.html")
cleantext = BeautifulSoup(f, "lxml").text
f.write(cleantext)
f.close()
