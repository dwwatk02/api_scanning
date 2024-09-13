#!/usr/bin/env python3
import http.client
import sys

conn = http.client.HTTPSConnection("api.secured-api.com")

domain = sys.argv[1]
headers = {
    'accept': "application/json, text/x-yaml",
    'Authorization': "Bearer <bearer token>"
    }

conn.request("GET", "/v1/inventory/oas-swagger?hostname="+domain, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
