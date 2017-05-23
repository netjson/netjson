all:
	python preprocess.py
	xml2rfc -b netjson netjson-preprocessed.xml
	xml2rfc --html -b netjson netjson-preprocessed.xml

google_analytics:
	python add_ga.py

epub:
	ebook-convert netjson.html netjson.epub

clean:
	rm -f netjson-preprocessed.xml netjson.txt netjson.html netjson.epub
