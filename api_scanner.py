#!/usr/bin/python3

from asoc_api import ASoC
import urllib3
import json

urllib3.disable_warnings()

## ------ please edit variables in this block -----
#API Key
keyId=""
keySecret=""
## path to (newline-delimited) text file containing domain names
collection_file="/Users/davidwatkins/api_security/demo.testfire.collection.json"
app_id = "a384f3bf-e585-4e34-960c-21b4b50c79e9"
starting_url = "https://demo.testfire.net/"
scan_name = "testpostman"

## ------------------------------------------------

## ------ please do NOT edit anything below  -----
## authenticate
asoc = ASoC(keyId, keySecret)
code, result = asoc.login()
if code != 200:
	print(f'error logging into ASOC!! code is {code}')

file_id = asoc.uploadCollectionFile(collection_file)["FileId"]

asoc.createDastScan(app_id,file_id,starting_url,scan_name)