#How to send data to the api

first run the app:

python app.py

then do a post request to the backend:

In python:

import requests
import json
data = {'data':'element'}
requests.post("http://localhost:5000/api/test/+json.dumps(data))



