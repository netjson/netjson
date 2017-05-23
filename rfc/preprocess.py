#!/usr/bin/env python
import os

text = ''
with open('netjson.xml', 'r') as xml:
    text = xml.read()

includes = ['../examples/{0}'.format(f) for f in  os.listdir('../examples')]

for include in includes:
    with open(include, 'r') as include_file:
        included_text = include_file.read()
    include_statement = '{{ %s }}' % include
    text = text.replace(include_statement, included_text)

with open('netjson-preprocessed.xml', 'w') as xml:
    xml.write(text)
