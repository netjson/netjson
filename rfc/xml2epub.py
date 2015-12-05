#!/bin/env python
import requests

form_url = 'http://xml2rfc.ietf.org/cgi-bin/xml2rfc.cgi'
params = {
    "url": "https://raw.githubusercontent.com/interop-dev/netjson/master/rfc/netjson.xml",
    "modeAsFormat": "html/epub"
}

response = requests.post(form_url, params)
if response.status_code == 200:
    f = open('./netjson.epub', 'w')
    f.write(response.content)
    f.close()
    print('Generated RFC in ePub format')
else:
    print("Error: response code was: {0}".format(response.status_code))
