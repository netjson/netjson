all:
	./preprocess.py
	xml2rfc netjson-preprocessed.xml
	xml2rfc --html netjson-preprocessed.xml
	python add_ga.py
	python xml2epub.py

clean:
	rm -f netjson-preprocessed.xml netjson.txt netjson.html netjson.epub
