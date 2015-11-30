#!/bin/env python
import requests

form_url = 'http://xml2rfc.ietf.org/cgi-bin/xml2rfc.cgi'
params = {
    "url": "https://raw.githubusercontent.com/interop-dev/netjson/master/rfc/netjson.xml",
    "modeAsFormat": "html/epub"
}

response = requests.post(form_url, params)
f = open('./rfc.epub', 'w')
f.write(response.content)
f.close()
