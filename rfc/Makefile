all: rfc google_analytics epub publish

rfc:
	python preprocess.py
	xml2rfc netjson-preprocessed.xml
	xml2rfc --html netjson-preprocessed.xml
	mv netjson-preprocessed.html netjson.html

google_analytics:
	python add_ga.py

epub:
	ebook-convert netjson.html netjson.epub

publish:
	mv netjson.html ../website/rfc.html
	cp netjson.xml ../website/rfc.xml
	mv netjson.epub ../website/rfc.epub

clean:
	rm -f netjson-preprocessed.xml netjson.txt netjson.html netjson.epub
