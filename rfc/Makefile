all: netjson.xml
	xml2rfc netjson.xml
	xml2rfc --html netjson.xml
	python xml2epub.py

clean:
	rm -f netjson.txt netjson.html netjson.epub
